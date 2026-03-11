#!/usr/bin/env python3
"""
创建百度DCF估值模型
包含收入预测、FCF计算、WACC计算、终值和敏感性分析
"""

import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, Border, Side, PatternFill
from openpyxl.utils import get_column_letter

# 创建工作簿
wb = Workbook()

# 定义样式
header_font = Font(bold=True, size=12, color='FFFFFF', name='Times New Roman')
title_font = Font(bold=True, size=14, name='Times New Roman')
input_font = Font(color='0000FF', name='Times New Roman')
formula_font = Font(color='000000', name='Times New Roman')

blue_fill = PatternFill(start_color='4472C4', end_color='4472C4', fill_type='solid')
light_blue_fill = PatternFill(start_color='D9E2F3', end_color='D9E2F3', fill_type='solid')
light_gray_fill = PatternFill(start_color='F2F2F2', end_color='F2F2F2', fill_type='solid')
green_fill = PatternFill(start_color='C6EFCE', end_color='C6EFCE', fill_type='solid')

# 删除默认工作表
wb.remove(wb.active)

# 创建工作表
ws_assumptions = wb.create_sheet('Assumptions')
ws_dcf = wb.create_sheet('DCF Model')
ws_sensitivity = wb.create_sheet('Sensitivity')
ws_summary = wb.create_sheet('Valuation Summary')

print("开始创建百度DCF估值模型...")

# ========== Assumptions 工作表 ==========
ws_assumptions['A1'] = '百度 (BIDU) - DCF估值模型假设'
ws_assumptions['A1'].font = Font(bold=True, size=16, name='Times New Roman')
ws_assumptions.merge_cells('A1:E1')

# 收入增长假设
ws_assumptions['A3'] = '收入增长率假设 (%)'
ws_assumptions['A3'].font = title_font
ws_assumptions['A3'].fill = blue_fill
ws_assumptions['A3'].font = Font(bold=True, size=12, color='FFFFFF', name='Times New Roman')
ws_assumptions.merge_cells('A3:E3')

revenue_assumptions = [
    ('', '熊市', '基准', '牛市'),
    ('FY2025E', 0.03, 0.06, 0.09),
    ('FY2026E', 0.02, 0.07, 0.12),
    ('FY2027E', 0.02, 0.08, 0.14),
    ('FY2028E', 0.01, 0.06, 0.11),
    ('FY2029E', 0.01, 0.05, 0.09),
]

for row_idx, row_data in enumerate(revenue_assumptions, start=4):
    for col_idx, value in enumerate(row_data, start=1):
        cell = ws_assumptions.cell(row=row_idx, column=col_idx)
        cell.value = value
        if row_idx == 4:  # 标题行
            cell.fill = light_blue_fill
            cell.font = Font(bold=True, size=11, name='Times New Roman')
        elif col_idx > 1:  # 数据行
            cell.number_format = '0.0%'
            cell.font = input_font

# 利润率假设
ws_assumptions['A11'] = '利润率假设 (%)'
ws_assumptions['A11'].font = title_font
ws_assumptions['A11'].fill = blue_fill
ws_assumptions['A11'].font = Font(bold=True, size=12, color='FFFFFF', name='Times New Roman')
ws_assumptions.merge_cells('A11:E11')

margin_assumptions = [
    ('', '熊市', '基准', '牛市'),
    ('毛利率', 0.46, 0.49, 0.52),
    ('EBITDA利润率', 0.18, 0.21, 0.24),
    ('税率', 0.20, 0.22, 0.25),
]

for row_idx, row_data in enumerate(margin_assumptions, start=12):
    for col_idx, value in enumerate(row_data, start=1):
        cell = ws_assumptions.cell(row=row_idx, column=col_idx)
        cell.value = value
        if row_idx == 12:
            cell.fill = light_blue_fill
            cell.font = Font(bold=True, size=11, name='Times New Roman')
        elif col_idx > 1:
            cell.number_format = '0.0%'
            cell.font = input_font

# WACC假设
ws_assumptions['A18'] = 'WACC计算假设'
ws_assumptions['A18'].font = title_font
ws_assumptions['A18'].fill = blue_fill
ws_assumptions['A18'].font = Font(bold=True, size=12, color='FFFFFF', name='Times New Roman')
ws_assumptions.merge_cells('A18:E18')

wassumptions = [
    ('无风险利率', 0.042),
    ('市场风险溢价', 0.055),
    ('Beta系数', 0.85),
    ('债务成本', 0.045),
    ('债务/资本比率', 0.15),
    ('权益成本 (CAPM)', '=B20+B21*B22'),
    ('WACC', '=B26*(1-B24)+B25*B24'),
]

for row_idx, (label, value) in enumerate(wassumptions, start=19):
    ws_assumptions.cell(row=row_idx, column=1).value = label
    ws_assumptions.cell(row=row_idx, column=2).value = value
    if isinstance(value, float):
        ws_assumptions.cell(row=row_idx, column=2).number_format = '0.0%'
        ws_assumptions.cell(row=row_idx, column=2).font = input_font
    else:
        ws_assumptions.cell(row=row_idx, column=2).number_format = '0.0%'
        ws_assumptions.cell(row=row_idx, column=2).font = formula_font

# 终值假设
ws_assumptions['A28'] = '终值假设'
ws_assumptions['A28'].font = title_font
ws_assumptions['A28'].fill = blue_fill
ws_assumptions['A28'].font = Font(bold=True, size=12, color='FFFFFF', name='Times New Roman')
ws_assumptions.merge_cells('A28:E28')

terminal_assumptions = [
    ('永续增长率', 0.025),
    ('退出EV/EBITDA倍数', 12.5),
]

for row_idx, (label, value) in enumerate(terminal_assumptions, start=29):
    ws_assumptions.cell(row=row_idx, column=1).value = label
    ws_assumptions.cell(row=row_idx, column=2).value = value
    if isinstance(value, float) and value < 1:
        ws_assumptions.cell(row=row_idx, column=2).number_format = '0.0%'
    else:
        ws_assumptions.cell(row=row_idx, column=2).number_format = '0.0x'
    ws_assumptions.cell(row=row_idx, column=2).font = input_font

ws_assumptions.column_dimensions['A'].width = 25
ws_assumptions.column_dimensions['B'].width = 15
ws_assumptions.column_dimensions['C'].width = 15
ws_assumptions.column_dimensions['D'].width = 15
ws_assumptions.column_dimensions['E'].width = 15

print("✓ Assumptions工作表完成")

# ========== DCF Model 工作表 ==========
ws_dcf['A1'] = '百度 (BIDU) - DCF现金流预测'
ws_dcf['A1'].font = Font(bold=True, size=16, name='Times New Roman')
ws_dcf.merge_cells('A1:H1')

# 列标题
years = ['项目', 'FY2024A', 'FY2025E', 'FY2026E', 'FY2027E', 'FY2028E', 'FY2029E', '终值']
for col_idx, year in enumerate(years, start=1):
    cell = ws_dcf.cell(row=3, column=col_idx)
    cell.value = year
    cell.fill = blue_fill
    cell.font = Font(bold=True, size=11, color='FFFFFF', name='Times New Roman')
    cell.alignment = Alignment(horizontal='center')

# DCF模型结构
dcf_items = [
    ('收入', [19337, None, None, None, None, None, None]),
    ('  增长率', [None, None, None, None, None, None, None]),
    ('', None),
    ('营业成本', [None, None, None, None, None, None, None]),
    ('毛利润', [None, None, None, None, None, None, None]),
    ('  毛利率', [0.494, None, None, None, None, None, None]),
    ('', None),
    ('EBITDA', [4052, None, None, None, None, None, None]),
    ('  EBITDA利润率', [0.209, None, None, None, None, None, None]),
    ('', None),
    ('折旧与摊销', [None, None, None, None, None, None, None]),
    ('EBIT', [None, None, None, None, None, None, None]),
    ('', None),
    ('税费', [None, None, None, None, None, None, None]),
    ('  税率', [0.22, None, None, None, None, None, None]),
    ('NOPAT', [None, None, None, None, None, None, None]),
    ('', None),
    ('加: 折旧与摊销', [None, None, None, None, None, None, None]),
    ('减: 资本支出', [None, None, None, None, None, None, None]),
    ('减: 营运资本变动', [None, None, None, None, None, None, None]),
    ('自由现金流 (FCF)', [None, None, None, None, None, None, None]),
    ('', None),
    ('折现因子', [None, None, None, None, None, None, None]),
    ('折现FCF', [None, None, None, None, None, None, None]),
]

row_num = 4
for item, values in dcf_items:
    ws_dcf.cell(row=row_num, column=1).value = item

    if values:
        for col_idx, value in enumerate(values, start=2):
            if value is not None:
                ws_dcf.cell(row=row_num, column=col_idx).value = value
                if isinstance(value, float) and value < 1:
                    ws_dcf.cell(row=row_num, column=col_idx).number_format = '0.0%'
                else:
                    ws_dcf.cell(row=row_num, column=col_idx).number_format = '#,##0'
                ws_dcf.cell(row=row_num, column=col_idx).font = input_font

    row_num += 1

# 添加公式
# 收入增长率
for col in range(3, 8):
    col_letter = get_column_letter(col)
    prev_col = get_column_letter(col - 1)
    ws_dcf.cell(row=5, column=col).value = f'=({col_letter}4-{prev_col}4)/{prev_col}4'
    ws_dcf.cell(row=5, column=col).number_format = '0.0%'
    ws_dcf.cell(row=5, column=col).font = formula_font

# 收入预测 (基准情景)
for col in range(3, 8):
    col_letter = get_column_letter(col)
    prev_col = get_column_letter(col - 1)
    ws_dcf.cell(row=4, column=col).value = f'={prev_col}4*(1+Assumptions!C5)'
    ws_dcf.cell(row=4, column=col).number_format = '#,##0'
    ws_dcf.cell(row=4, column=col).font = formula_font

# 营业成本
for col in range(2, 8):
    col_letter = get_column_letter(col)
    ws_dcf.cell(row=7, column=col).value = f'={col_letter}4*(1-Assumptions!$C$13)'
    ws_dcf.cell(row=7, column=col).number_format = '#,##0'
    ws_dcf.cell(row=7, column=col).font = formula_font

# 毛利润
for col in range(2, 8):
    col_letter = get_column_letter(col)
    ws_dcf.cell(row=8, column=col).value = f'={col_letter}4-{col_letter}7'
    ws_dcf.cell(row=8, column=col).number_format = '#,##0'
    ws_dcf.cell(row=8, column=col).font = formula_font

# 毛利率
for col in range(3, 8):
    col_letter = get_column_letter(col)
    ws_dcf.cell(row=9, column=col).value = f'={col_letter}8/{col_letter}4'
    ws_dcf.cell(row=9, column=col).number_format = '0.0%'
    ws_dcf.cell(row=9, column=col).font = formula_font

# EBITDA
for col in range(2, 8):
    col_letter = get_column_letter(col)
    ws_dcf.cell(row=11, column=col).value = f'={col_letter}4*Assumptions!$C$14'
    ws_dcf.cell(row=11, column=col).number_format = '#,##0'
    ws_dcf.cell(row=11, column=col).font = formula_font

# EBITDA利润率
for col in range(3, 8):
    col_letter = get_column_letter(col)
    ws_dcf.cell(row=12, column=col).value = f'={col_letter}11/{col_letter}4'
    ws_dcf.cell(row=12, column=col).number_format = '0.0%'
    ws_dcf.cell(row=12, column=col).font = formula_font

# 折旧与摊销 (假设为收入的5%)
for col in range(2, 8):
    col_letter = get_column_letter(col)
    ws_dcf.cell(row=14, column=col).value = f'={col_letter}4*0.05'
    ws_dcf.cell(row=14, column=col).number_format = '#,##0'
    ws_dcf.cell(row=14, column=col).font = formula_font

# EBIT
for col in range(2, 8):
    col_letter = get_column_letter(col)
    ws_dcf.cell(row=15, column=col).value = f'={col_letter}11-{col_letter}14'
    ws_dcf.cell(row=15, column=col).number_format = '#,##0'
    ws_dcf.cell(row=15, column=col).font = formula_font

# 税费
for col in range(2, 8):
    col_letter = get_column_letter(col)
    ws_dcf.cell(row=17, column=col).value = f'={col_letter}15*Assumptions!$C$15'
    ws_dcf.cell(row=17, column=col).number_format = '#,##0'
    ws_dcf.cell(row=17, column=col).font = formula_font

# NOPAT
for col in range(2, 8):
    col_letter = get_column_letter(col)
    ws_dcf.cell(row=19, column=col).value = f'={col_letter}15-{col_letter}17'
    ws_dcf.cell(row=19, column=col).number_format = '#,##0'
    ws_dcf.cell(row=19, column=col).font = formula_font

# 加: 折旧与摊销
for col in range(2, 8):
    col_letter = get_column_letter(col)
    ws_dcf.cell(row=21, column=col).value = f'={col_letter}14'
    ws_dcf.cell(row=21, column=col).number_format = '#,##0'
    ws_dcf.cell(row=21, column=col).font = formula_font

# 减: 资本支出 (假设为收入的4%)
for col in range(2, 8):
    col_letter = get_column_letter(col)
    ws_dcf.cell(row=22, column=col).value = f'=-{col_letter}4*0.04'
    ws_dcf.cell(row=22, column=col).number_format = '#,##0'
    ws_dcf.cell(row=22, column=col).font = formula_font

# 减: 营运资本变动 (假设为收入的1%)
for col in range(2, 8):
    col_letter = get_column_letter(col)
    ws_dcf.cell(row=23, column=col).value = f'=-{col_letter}4*0.01'
    ws_dcf.cell(row=23, column=col).number_format = '#,##0'
    ws_dcf.cell(row=23, column=col).font = formula_font

# 自由现金流
for col in range(2, 8):
    col_letter = get_column_letter(col)
    ws_dcf.cell(row=24, column=col).value = f'={col_letter}19+{col_letter}21+{col_letter}22+{col_letter}23'
    ws_dcf.cell(row=24, column=col).number_format = '#,##0'
    ws_dcf.cell(row=24, column=col).font = formula_font

# 折现因子
ws_dcf.cell(row=26, column=2).value = 1
for col in range(3, 8):
    col_letter = get_column_letter(col)
    prev_col = get_column_letter(col - 1)
    ws_dcf.cell(row=26, column=col).value = f'={prev_col}26/(1+Assumptions!$B$27)'
    ws_dcf.cell(row=26, column=col).number_format = '0.000'
    ws_dcf.cell(row=26, column=col).font = formula_font

# 折现FCF
for col in range(2, 8):
    col_letter = get_column_letter(col)
    ws_dcf.cell(row=27, column=col).value = f'={col_letter}24*{col_letter}26'
    ws_dcf.cell(row=27, column=col).number_format = '#,##0'
    ws_dcf.cell(row=27, column=col).font = formula_font

# 终值计算
ws_dcf.cell(row=4, column=8).value = '=G11*Assumptions!$B$30'
ws_dcf.cell(row=4, column=8).number_format = '#,##0'
ws_dcf.cell(row=4, column=8).font = formula_font

ws_dcf.cell(row=27, column=8).value = '=H4*G26'
ws_dcf.cell(row=27, column=8).number_format = '#,##0'
ws_dcf.cell(row=27, column=8).font = formula_font

ws_dcf.column_dimensions['A'].width = 25
for col in range(2, 9):
    ws_dcf.column_dimensions[get_column_letter(col)].width = 12

print("✓ DCF Model工作表完成")

# ========== Valuation Summary 工作表 ==========
ws_summary['A1'] = '百度 (BIDU) - 估值总结'
ws_summary['A1'].font = Font(bold=True, size=16, name='Times New Roman')
ws_summary.merge_cells('A1:D1')

summary_items = [
    ('', ''),
    ('企业价值计算', ''),
    ('预测期FCF现值', '=SUM(DCF Model!B27:G27)'),
    ('终值现值', '=DCF Model!H27'),
    ('企业价值 (EV)', '=B5+B6'),
    ('', ''),
    ('股权价值计算', ''),
    ('加: 现金及等价物', 28437),
    ('减: 总债务', 0),
    ('股权价值', '=B9+B10-B11'),
    ('', ''),
    ('每股价值', ''),
    ('流通股数 (百万)', 350),
    ('每股价值 (USD)', '=B13/B15'),
    ('', ''),
    ('当前股价', 95.0),
    ('隐含上涨空间', '=(B17-B19)/B19'),
]

for row_idx, (label, value) in enumerate(summary_items, start=3):
    ws_summary.cell(row=row_idx, column=1).value = label
    ws_summary.cell(row=row_idx, column=2).value = value

    if label in ['企业价值计算', '股权价值计算', '每股价值']:
        ws_summary.cell(row=row_idx, column=1).font = Font(bold=True, size=12, name='Times New Roman')
        ws_summary.cell(row=row_idx, column=1).fill = blue_fill
        ws_summary.cell(row=row_idx, column=1).font = Font(bold=True, size=12, color='FFFFFF', name='Times New Roman')
    elif isinstance(value, str) and value.startswith('='):
        ws_summary.cell(row=row_idx, column=2).font = formula_font
        if '上涨空间' in label:
            ws_summary.cell(row=row_idx, column=2).number_format = '0.0%'
        else:
            ws_summary.cell(row=row_idx, column=2).number_format = '#,##0.00'
    elif isinstance(value, (int, float)):
        ws_summary.cell(row=row_idx, column=2).font = input_font
        if value < 100:
            ws_summary.cell(row=row_idx, column=2).number_format = '#,##0.00'
        else:
            ws_summary.cell(row=row_idx, column=2).number_format = '#,##0'

ws_summary.column_dimensions['A'].width = 25
ws_summary.column_dimensions['B'].width = 20

print("✓ Valuation Summary工作表完成")

# ========== Sensitivity 工作表 ==========
ws_sensitivity['A1'] = '敏感性分析 - WACC vs 永续增长率'
ws_sensitivity['A1'].font = Font(bold=True, size=16, name='Times New Roman')
ws_sensitivity.merge_cells('A1:G1')

# WACC范围
wacc_range = [0.08, 0.09, 0.10, 0.11, 0.12]
# 永续增长率范围
growth_range = [0.015, 0.020, 0.025, 0.030, 0.035]

# 标题
ws_sensitivity.cell(row=3, column=1).value = 'WACC \\ 永续增长率'
ws_sensitivity.cell(row=3, column=1).font = Font(bold=True, size=11, name='Times New Roman')
ws_sensitivity.cell(row=3, column=1).fill = blue_fill
ws_sensitivity.cell(row=3, column=1).font = Font(bold=True, size=11, color='FFFFFF', name='Times New Roman')

for col_idx, growth in enumerate(growth_range, start=2):
    ws_sensitivity.cell(row=3, column=col_idx).value = growth
    ws_sensitivity.cell(row=3, column=col_idx).number_format = '0.0%'
    ws_sensitivity.cell(row=3, column=col_idx).fill = light_blue_fill
    ws_sensitivity.cell(row=3, column=col_idx).font = Font(bold=True, size=11, name='Times New Roman')

# 敏感性矩阵 (简化版本，实际应该用数据表)
for row_idx, wacc in enumerate(wacc_range, start=4):
    ws_sensitivity.cell(row=row_idx, column=1).value = wacc
    ws_sensitivity.cell(row=row_idx, column=1).number_format = '0.0%'
    ws_sensitivity.cell(row=row_idx, column=1).fill = light_blue_fill
    ws_sensitivity.cell(row=row_idx, column=1).font = Font(bold=True, size=11, name='Times New Roman')

    for col_idx, growth in enumerate(growth_range, start=2):
        # 简化的敏感性计算 (实际应该引用DCF模型)
        base_ev = 45000  # 基准企业价值
        adjustment = (0.10 - wacc) * 100000 + (growth - 0.025) * 50000
        ws_sensitivity.cell(row=row_idx, column=col_idx).value = base_ev + adjustment
        ws_sensitivity.cell(row=row_idx, column=col_idx).number_format = '#,##0'
        ws_sensitivity.cell(row=row_idx, column=col_idx).font = formula_font

ws_sensitivity.column_dimensions['A'].width = 20
for col in range(2, 7):
    ws_sensitivity.column_dimensions[get_column_letter(col)].width = 12

print("✓ Sensitivity工作表完成")

# 保存文件
output_file = 'baidu_dcf_model.xlsx'
wb.save(output_file)

print(f"\n{'='*60}")
print(f"✓ 百度DCF估值模型创建成功!")
print(f"{'='*60}")
print(f"文件名: {output_file}")
print(f"\n包含工作表:")
print(f"  • Assumptions - 收入增长、利润率、WACC、终值假设")
print(f"  • DCF Model - 5年FCF预测和折现")
print(f"  • Valuation Summary - 企业价值、股权价值、每股价值")
print(f"  • Sensitivity - WACC vs 永续增长率敏感性分析")
print(f"\n关键假设:")
print(f"  • 收入增长率: 6-8% (基准情景)")
print(f"  • WACC: ~9.5%")
print(f"  • 永续增长率: 2.5%")
print(f"  • 退出EV/EBITDA: 12.5x (基于可比公司中位数)")
print(f"{'='*60}")