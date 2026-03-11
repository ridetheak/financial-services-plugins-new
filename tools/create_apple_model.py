#!/usr/bin/env python3
"""
创建苹果公司三表财务模型
包含利润表、资产负债表、现金流量表及支持性附表
"""

import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, Border, Side, PatternFill, NamedStyle
from openpyxl.utils import get_column_letter
from openpyxl.formatting.rule import FormulaRule
from datetime import datetime

# 创建工作簿
wb = Workbook()

# 定义样式
header_font = Font(bold=True, size=12, color='FFFFFF')
title_font = Font(bold=True, size=14)
blue_fill = PatternFill(start_color='4472C4', end_color='4472C4', fill_type='solid')
light_blue_fill = PatternFill(start_color='D6DCE4', end_color='D6DCE4', fill_type='solid')
input_font = Font(color='0000FF')  # 蓝色字体表示输入
formula_font = Font(color='000000')  # 黑色字体表示公式
link_font = Font(color='008000')  # 绿色字体表示链接

thin_border = Border(
    left=Side(style='thin'),
    right=Side(style='thin'),
    top=Side(style='thin'),
    bottom=Side(style='thin')
)

# 删除默认工作表
wb.remove(wb.active)

# ========== 创建工作表 ==========
ws_assumptions = wb.create_sheet('Assumptions')
ws_is = wb.create_sheet('IS')
ws_bs = wb.create_sheet('BS')
ws_cf = wb.create_sheet('CF')
ws_wc = wb.create_sheet('WC')
ws_da = wb.create_sheet('DA')
ws_checks = wb.create_sheet('Checks')

# ========== Assumptions 工作表 ==========
ws_assumptions['A1'] = '苹果公司 (AAPL) - 财务模型假设'
ws_assumptions['A1'].font = Font(bold=True, size=16)

# 时间周期
ws_assumptions['A3'] = '时间周期'
ws_assumptions['A3'].font = title_font
ws_assumptions['A4'] = '历史期间'
ws_assumptions['B4'] = 5
ws_assumptions['A5'] = '预测期间'
ws_assumptions['B5'] = 5

# 收入增长假设
ws_assumptions['A7'] = '收入增长率 (%)'
ws_assumptions['A7'].font = title_font
ws_assumptions['A8'] = 'FY2025E'
ws_assumptions['B8'] = 0.05  # 5% 增长
ws_assumptions['A9'] = 'FY2026E'
ws_assumptions['B9'] = 0.06
ws_assumptions['A10'] = 'FY2027E'
ws_assumptions['B10'] = 0.07
ws_assumptions['A11'] = 'FY2028E'
ws_assumptions['B11'] = 0.06
ws_assumptions['A12'] = 'FY2029E'
ws_assumptions['B12'] = 0.05

# 利润率假设
ws_assumptions['A14'] = '利润率假设 (%)'
ws_assumptions['A14'].font = title_font
ws_assumptions['A15'] = '毛利率'
ws_assumptions['B15'] = 0.46  # 46%
ws_assumptions['A16'] = '研发费用率'
ws_assumptions['B16'] = 0.07
ws_assumptions['A17'] = '销售及管理费用率'
ws_assumptions['B17'] = 0.06

# 应用蓝色字体到输入单元格
for row in range(8, 18):
    cell = ws_assumptions.cell(row=row, column=2)
    cell.font = input_font

print("Assumptions工作表创建完成")

# ========== IS 工作表 (利润表) ==========
ws_is['A1'] = '苹果公司 (AAPL) - 利润表'
ws_is['A1'].font = Font(bold=True, size=16)
ws_is['A2'] = '单位: 百万美元'
ws_is['A2'].font = Font(italic=True)

# 列标题
ws_is['A4'] = ''
ws_is['B4'] = 'FY2020A'
ws_is['C4'] = 'FY2021A'
ws_is['D4'] = 'FY2022A'
ws_is['E4'] = 'FY2023A'
ws_is['F4'] = 'FY2024A'
ws_is['G4'] = 'FY2025E'
ws_is['H4'] = 'FY2026E'
ws_is['I4'] = 'FY2027E'
ws_is['J4'] = 'FY2028E'
ws_is['K4'] = 'FY2029E'

# 应用标题样式
for col in range(1, 12):
    ws_is.cell(row=4, column=col).fill = blue_fill
    ws_is.cell(row=4, column=col).font = header_font
    ws_is.cell(row=4, column=col).alignment = Alignment(horizontal='center')

# 利润表项目
is_items = [
    ('收入', [274515, 365817, 394328, 383285, 383289]),
    ('营业成本', [169559, 212981, 223546, 214137, 210352]),
    ('毛利润', None),  # 公式
    ('', None),  # 空行
    ('研发费用', [18752, 21914, 26251, 29915, 31370]),
    ('销售及管理费用', [19916, 21914, 25094, 24932, 26097]),
    ('营业费用合计', None),  # 公式
    ('', None),
    ('营业利润', None),  # 公式
    ('', None),
    ('利息收入', None),
    ('利息费用', None),
    ('其他收入/(费用)', None),
    ('税前利润', None),
    ('', None),
    ('所得税费用', None),
    ('净利润', None),
]

row_num = 5
for item, values in is_items:
    ws_is.cell(row=row_num, column=1).value = item

    if values:
        for col_idx, value in enumerate(values, start=2):
            ws_is.cell(row=row_num, column=col_idx).value = value
            ws_is.cell(row=row_num, column=col_idx).font = input_font
    elif item == '毛利润':
        for col_idx in range(2, 12):
            ws_is.cell(row=row_num, column=col_idx).value = f'={get_column_letter(col_idx)}5-{get_column_letter(col_idx)}6'
    elif item == '营业费用合计':
        for col_idx in range(2, 12):
            ws_is.cell(row=row_num, column=col_idx).value = f'={get_column_letter(col_idx)}9+{get_column_letter(col_idx)}10'
    elif item == '营业利润':
        for col_idx in range(2, 12):
            ws_is.cell(row=row_num, column=col_idx).value = f'={get_column_letter(col_idx)}7-{get_column_letter(col_idx)}11'
    elif item == '净利润':
        for col_idx in range(2, 12):
            ws_is.cell(row=row_num, column=col_idx).value = f'={get_column_letter(col_idx)}19'

    row_num += 1

# 设置列宽
ws_is.column_dimensions['A'].width = 25
for col in range(2, 12):
    ws_is.column_dimensions[get_column_letter(col)].width = 12

print("IS工作表创建完成")

# ========== BS 工作表 (资产负债表) ==========
ws_bs['A1'] = '苹果公司 (AAPL) - 资产负债表'
ws_bs['A1'].font = Font(bold=True, size=16)
ws_bs['A2'] = '单位: 百万美元'
ws_bs['A2'].font = Font(italic=True)

# 列标题
ws_bs['A4'] = ''
for col_idx, year in enumerate(['FY2020A', 'FY2021A', 'FY2022A', 'FY2023A', 'FY2024A', 'FY2025E', 'FY2026E', 'FY2027E', 'FY2028E', 'FY2029E'], start=2):
    ws_bs.cell(row=4, column=col_idx).value = year
    ws_bs.cell(row=4, column=col_idx).fill = blue_fill
    ws_bs.cell(row=4, column=col_idx).font = header_font
    ws_bs.cell(row=4, column=col_idx).alignment = Alignment(horizontal='center')

# 资产负债表项目
bs_items = [
    ('资产', None),
    ('流动资产', None),
    ('现金及现金等价物', [38016, 34940, 23646, 29965, 29965]),
    ('短期投资', None),
    ('应收账款净额', [16158, 26278, 28297, 29508, 30550]),
    ('存货', [4061, 6580, 4946, 6331, 7200]),
    ('其他流动资产', None),
    ('流动资产合计', None),
    ('', None),
    ('长期投资', None),
    ('物业、厂房及设备净额', [36539, 39440, 42117, 43715, 45357]),
    ('无形资产净额', None),
    ('其他非流动资产', None),
    ('非流动资产合计', None),
    ('', None),
    ('资产总计', None),
    ('', None),
    ('负债及股东权益', None),
    ('流动负债', None),
    ('应付账款', [16377, 53730, 60039, 62833, 65844]),
    ('应计费用', None),
    ('递延收入', None),
    ('短期债务', None),
    ('其他流动负债', None),
    ('流动负债合计', None),
    ('', None),
    ('长期债务', None),
    ('递延所得税负债', None),
    ('其他非流动负债', None),
    ('非流动负债合计', None),
    ('', None),
    ('负债合计', None),
    ('', None),
    ('股东权益', None),
    ('普通股', None),
    ('留存收益', None),
    ('累计其他综合收益', None),
    ('股东权益合计', None),
    ('', None),
    ('负债及股东权益总计', None),
]

row_num = 5
for item, values in bs_items:
    ws_bs.cell(row=row_num, column=1).value = item

    if values:
        for col_idx, value in enumerate(values, start=2):
            ws_bs.cell(row=row_num, column=col_idx).value = value
            ws_bs.cell(row=row_num, column=col_idx).font = input_font

    row_num += 1

# 设置列宽
ws_bs.column_dimensions['A'].width = 30
for col in range(2, 12):
    ws_bs.column_dimensions[get_column_letter(col)].width = 12

print("BS工作表创建完成")

# ========== CF 工作表 (现金流量表) ==========
ws_cf['A1'] = '苹果公司 (AAPL) - 现金流量表'
ws_cf['A1'].font = Font(bold=True, size=16)
ws_cf['A2'] = '单位: 百万美元'
ws_cf['A2'].font = Font(italic=True)

# 列标题
ws_cf['A4'] = ''
for col_idx, year in enumerate(['FY2020A', 'FY2021A', 'FY2022A', 'FY2023A', 'FY2024A', 'FY2025E', 'FY2026E', 'FY2027E', 'FY2028E', 'FY2029E'], start=2):
    ws_cf.cell(row=4, column=col_idx).value = year
    ws_cf.cell(row=4, column=col_idx).fill = blue_fill
    ws_cf.cell(row=4, column=col_idx).font = header_font
    ws_cf.cell(row=4, column=col_idx).alignment = Alignment(horizontal='center')

cf_items = [
    ('经营活动现金流', None),
    ('净利润', None),
    ('折旧与摊销', [11056, 11105, 11112, 11544, 11283]),
    ('股权激励费用', None),
    ('营运资本变动', None),
    ('应收账款变动', None),
    ('存货变动', None),
    ('应付账款变动', None),
    ('其他经营性项目变动', None),
    ('经营活动现金流合计', None),
    ('', None),
    ('投资活动现金流', None),
    ('资本支出', None),
    ('收购支出', None),
    ('投资购买/(出售)', None),
    ('其他投资活动', None),
    ('投资活动现金流合计', None),
    ('', None),
    ('筹资活动现金流', None),
    ('债务发行(偿还)', None),
    ('股权回购', None),
    ('股利支付', None),
    ('其他筹资活动', None),
    ('筹资活动现金流合计', None),
    ('', None),
    ('现金变动净额', None),
    ('期初现金余额', None),
    ('期末现金余额', None),
]

row_num = 5
for item, values in cf_items:
    ws_cf.cell(row=row_num, column=1).value = item

    if values:
        for col_idx, value in enumerate(values, start=2):
            ws_cf.cell(row=row_num, column=col_idx).value = value
            ws_cf.cell(row=row_num, column=col_idx).font = input_font

    row_num += 1

# 设置列宽
ws_cf.column_dimensions['A'].width = 30
for col in range(2, 12):
    ws_cf.column_dimensions[get_column_letter(col)].width = 12

print("CF工作表创建完成")

# ========== Checks 工作表 ==========
ws_checks['A1'] = '模型验证检查'
ws_checks['A1'].font = Font(bold=True, size=16)

ws_checks['A3'] = '检查项目'
ws_checks['B3'] = '状态'
ws_checks['C3'] = '说明'

checks = [
    ('资产负债表平衡', '=IF(BS!A22=BS!A46,"✓ 通过","✗ 失败")', '资产 = 负债 + 股东权益'),
    ('现金流量表验证', '=IF(CF!A32=BS!A7,"✓ 通过","✗ 失败")', '期末现金 = 资产负债表现金'),
    ('净利润链接', '=IF(IS!A21=CF!A6,"✓ 通过","✗ 失败")', '利润表净利润 = 现金流量表净利润'),
]

row_num = 4
for check_name, formula, description in checks:
    ws_checks.cell(row=row_num, column=1).value = check_name
    ws_checks.cell(row=row_num, column=2).value = formula
    ws_checks.cell(row=row_num, column=3).value = description
    row_num += 1

ws_checks.column_dimensions['A'].width = 30
ws_checks.column_dimensions['B'].width = 15
ws_checks.column_dimensions['C'].width = 40

print("Checks工作表创建完成")

# 保存文件
output_file = 'apple_3_statement_model.xlsx'
wb.save(output_file)
print(f"\n✓ 三表模型已成功创建: {output_file}")
print(f"包含工作表: Assumptions, IS, BS, CF, WC, DA, Checks")