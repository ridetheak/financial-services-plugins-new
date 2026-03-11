#!/usr/bin/env python3
"""
创建苹果公司完整的三表财务模型
包含预测公式、三表链接和验证检查
"""

import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, Border, Side, PatternFill
from openpyxl.utils import get_column_letter

# 创建工作簿
wb = Workbook()

# 定义样式
header_font = Font(bold=True, size=11, color='FFFFFF')
title_font = Font(bold=True, size=14)
section_font = Font(bold=True, size=11)
input_font = Font(color='0000FF')  # 蓝色字体 = 输入
formula_font = Font(color='000000')  # 黑色字体 = 公式

blue_fill = PatternFill(start_color='4472C4', end_color='4472C4', fill_type='solid')
light_blue_fill = PatternFill(start_color='D6DCE4', end_color='D6DCE4', fill_type='solid')
green_fill = PatternFill(start_color='C6EFCE', end_color='C6EFCE', fill_type='solid')
red_fill = PatternFill(start_color='FFC7CE', end_color='FFC7CE', fill_type='solid')

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
ws_checks = wb.create_sheet('Checks')

print("开始创建三表模型...")

# ========== Assumptions 工作表 ==========
ws_assumptions['A1'] = '苹果公司 (AAPL) - 财务模型假设'
ws_assumptions['A1'].font = Font(bold=True, size=16)
ws_assumptions.merge_cells('A1:D1')

# 历史年份和预测年份
years = ['FY2020A', 'FY2021A', 'FY2022A', 'FY2023A', 'FY2024A',
         'FY2025E', 'FY2026E', 'FY2027E', 'FY2028E', 'FY2029E']

# 收入增长率假设
ws_assumptions['A3'] = '收入增长率 (%)'
ws_assumptions['A3'].font = title_font

revenue_growth = [None, None, None, None, None, 0.05, 0.06, 0.07, 0.06, 0.05]
for idx, growth in enumerate(revenue_growth):
    if growth is not None:
        ws_assumptions.cell(row=4, column=idx+2).value = growth
        ws_assumptions.cell(row=4, column=idx+2).font = input_font
        ws_assumptions.cell(row=4, column=idx+2).number_format = '0.0%'

ws_assumptions['A4'] = 'FY2020-FY2029'
ws_assumptions['B4'] = '增长率'

# 利润率假设
ws_assumptions['A6'] = '利润率假设 (%)'
ws_assumptions['A6'].font = title_font

margin_items = [
    ('毛利率', 0.46),
    ('研发费用率', 0.07),
    ('销售及管理费用率', 0.06),
    ('有效税率', 0.15),
]

row_num = 7
for item, value in margin_items:
    ws_assumptions.cell(row=row_num, column=1).value = item
    ws_assumptions.cell(row=row_num, column=2).value = value
    ws_assumptions.cell(row=row_num, column=2).font = input_font
    ws_assumptions.cell(row=row_num, column=2).number_format = '0.0%'
    row_num += 1

# 营运资本假设
ws_assumptions['A12'] = '营运资本假设 (天数)'
ws_assumptions['A12'].font = title_font

wc_items = [
    ('应收账款周转天数 (DSO)', 40),
    ('存货周转天数 (DIO)', 10),
    ('应付账款周转天数 (DPO)', 60),
]

row_num = 13
for item, value in wc_items:
    ws_assumptions.cell(row=row_num, column=1).value = item
    ws_assumptions.cell(row=row_num, column=2).value = value
    ws_assumptions.cell(row=row_num, column=2).font = input_font
    row_num += 1

# 其他假设
ws_assumptions['A17'] = '其他假设'
ws_assumptions['A17'].font = title_font

other_items = [
    ('资本支出占收入比例', 0.03),
    ('折旧占资本支出比例', 0.95),
    ('股利支付率', 0.15),
]

row_num = 18
for item, value in other_items:
    ws_assumptions.cell(row=row_num, column=1).value = item
    ws_assumptions.cell(row=row_num, column=2).value = value
    ws_assumptions.cell(row=row_num, column=2).font = input_font
    ws_assumptions.cell(row=row_num, column=2).number_format = '0.0%'
    row_num += 1

ws_assumptions.column_dimensions['A'].width = 35
ws_assumptions.column_dimensions['B'].width = 15

print("✓ Assumptions工作表完成")

# ========== IS 工作表 (利润表) ==========
ws_is['A1'] = '苹果公司 (AAPL) - 利润表'
ws_is['A1'].font = Font(bold=True, size=16)
ws_is['A2'] = '单位: 百万美元'
ws_is['A2'].font = Font(italic=True)

# 列标题
ws_is['A4'] = ''
for idx, year in enumerate(years):
    col_letter = get_column_letter(idx + 2)
    ws_is.cell(row=4, column=idx+2).value = year
    ws_is.cell(row=4, column=idx+2).fill = blue_fill
    ws_is.cell(row=4, column=idx+2).font = header_font
    ws_is.cell(row=4, column=idx+2).alignment = Alignment(horizontal='center')

# 利润表项目 - 历史数据
is_structure = {
    5: ('收入', [274515, 365817, 394328, 383285, 383289]),
    6: ('营业成本', [169559, 212981, 223546, 214137, 210352]),
    7: ('毛利润', 'formula'),  # B5-B6
    8: ('', None),
    9: ('研发费用', [18752, 21914, 26251, 29915, 31370]),
    10: ('销售及管理费用', [19916, 21914, 25094, 24932, 26097]),
    11: ('营业费用合计', 'formula'),  # B9+B10
    12: ('', None),
    13: ('营业利润', 'formula'),  # B7-B11
    14: ('', None),
    15: ('利息收入', [2444, 3543, 3810, 3762, 3762]),
    16: ('利息费用', [-2571, -2645, -2931, -3933, -3933]),
    17: ('其他收入/(费用)', [None, None, None, None, None]),
    18: ('税前利润', 'formula'),  # B13+B15+B16+B17
    19: ('', None),
    20: ('所得税费用', None),  # 待计算
    21: ('净利润', 'formula'),  # B18-B20
    22: ('', None),
    23: ('毛利率 (%)', 'margin'),  # B7/B5
    24: ('营业利润率 (%)', 'margin'),  # B13/B5
    25: ('净利润率 (%)', 'margin'),  # B21/B5
}

for row_num, (item, values) in is_structure.items():
    ws_is.cell(row=row_num, column=1).value = item

    if values == 'formula':
        # 公式计算
        if row_num == 7:  # 毛利润
            for col in range(2, 12):
                col_letter = get_column_letter(col)
                ws_is.cell(row=row_num, column=col).value = f'={col_letter}5-{col_letter}6'
        elif row_num == 11:  # 营业费用合计
            for col in range(2, 12):
                col_letter = get_column_letter(col)
                ws_is.cell(row=row_num, column=col).value = f'={col_letter}9+{col_letter}10'
        elif row_num == 13:  # 营业利润
            for col in range(2, 12):
                col_letter = get_column_letter(col)
                ws_is.cell(row=row_num, column=col).value = f'={col_letter}7-{col_letter}11'
        elif row_num == 18:  # 税前利润
            for col in range(2, 12):
                col_letter = get_column_letter(col)
                ws_is.cell(row=row_num, column=col).value = f'={col_letter}13+{col_letter}15+{col_letter}16'
        elif row_num == 21:  # 净利润
            for col in range(2, 12):
                col_letter = get_column_letter(col)
                ws_is.cell(row=row_num, column=col).value = f'={col_letter}18-{col_letter}20'

    elif values == 'margin':
        # 利润率计算
        if row_num == 23:  # 毛利率
            for col in range(2, 12):
                col_letter = get_column_letter(col)
                ws_is.cell(row=row_num, column=col).value = f'={col_letter}7/{col_letter}5'
                ws_is.cell(row=row_num, column=col).number_format = '0.0%'
        elif row_num == 24:  # 营业利润率
            for col in range(2, 12):
                col_letter = get_column_letter(col)
                ws_is.cell(row=row_num, column=col).value = f'={col_letter}13/{col_letter}5'
                ws_is.cell(row=row_num, column=col).number_format = '0.0%'
        elif row_num == 25:  # 净利润率
            for col in range(2, 12):
                col_letter = get_column_letter(col)
                ws_is.cell(row=row_num, column=col).value = f'={col_letter}21/{col_letter}5'
                ws_is.cell(row=row_num, column=col).number_format = '0.0%'

    elif isinstance(values, list):
        # 历史数据
        for col_idx, value in enumerate(values):
            if value is not None:
                ws_is.cell(row=row_num, column=col_idx+2).value = value
                ws_is.cell(row=row_num, column=col_idx+2).font = input_font

# 添加预测公式
# 收入预测 - 基于增长率
for col in range(7, 12):  # FY2025E to FY2029E
    col_letter = get_column_letter(col)
    prev_col = get_column_letter(col - 1)
    growth_rate = f'Assumptions!{get_column_letter(col)}4'
    ws_is.cell(row=5, column=col).value = f'={prev_col}5*(1+{growth_rate})'
    ws_is.cell(row=5, column=col).font = formula_font

# 营业成本预测 - 基于毛利率
for col in range(7, 12):
    col_letter = get_column_letter(col)
    ws_is.cell(row=6, column=col).value = f'={col_letter}5*(1-Assumptions!$B$7)'
    ws_is.cell(row=6, column=col).font = formula_font

# 研发费用预测 - 基于费用率
for col in range(7, 12):
    col_letter = get_column_letter(col)
    ws_is.cell(row=9, column=col).value = f'={col_letter}5*Assumptions!$B$8'
    ws_is.cell(row=9, column=col).font = formula_font

# 销售及管理费用预测
for col in range(7, 12):
    col_letter = get_column_letter(col)
    ws_is.cell(row=10, column=col).value = f'={col_letter}5*Assumptions!$B$9'
    ws_is.cell(row=10, column=col).font = formula_font

# 所得税计算
for col in range(2, 12):
    col_letter = get_column_letter(col)
    ws_is.cell(row=20, column=col).value = f'=MAX(0,{col_letter}18)*Assumptions!$B$10'
    ws_is.cell(row=20, column=col).font = formula_font

# 利息收入和利息费用保持历史水平
for col in range(7, 12):
    ws_is.cell(row=15, column=col).value = f'={get_column_letter(col-1)}15'
    ws_is.cell(row=16, column=col).value = f'={get_column_letter(col-1)}16'

ws_is.column_dimensions['A'].width = 25
for col in range(2, 12):
    ws_is.column_dimensions[get_column_letter(col)].width = 12

print("✓ IS工作表完成")

# ========== BS 工作表 (资产负债表) ==========
ws_bs['A1'] = '苹果公司 (AAPL) - 资产负债表'
ws_bs['A1'].font = Font(bold=True, size=16)
ws_bs['A2'] = '单位: 百万美元'
ws_bs['A2'].font = Font(italic=True)

# 列标题
ws_bs['A4'] = ''
for idx, year in enumerate(years):
    ws_bs.cell(row=4, column=idx+2).value = year
    ws_bs.cell(row=4, column=idx+2).fill = blue_fill
    ws_bs.cell(row=4, column=idx+2).font = header_font
    ws_bs.cell(row=4, column=idx+2).alignment = Alignment(horizontal='center')

# 资产负债表结构
bs_structure = {
    # 资产
    5: ('资产', None),
    6: ('流动资产', None),
    7: ('  现金及现金等价物', [38016, 34940, 23646, 29965, 29965]),
    8: ('  短期投资', [37368, 27699, 24658, 31587, 29135]),
    9: ('  应收账款净额', [16158, 26278, 28297, 29508, 30550]),
    10: ('  存货', [4061, 6580, 4946, 6331, 7200]),
    11: ('  其他流动资产', [32688, 35677, 37479, 40388, 42411]),
    12: ('流动资产合计', 'formula'),  # SUM
    13: ('', None),
    14: ('非流动资产', None),
    15: ('  长期投资', [100887, 127877, 120605, 100544, 94378]),
    16: ('  物业、厂房及设备净额', [36539, 39440, 42117, 43715, 45357]),
    17: ('  无形资产净额', None),
    18: ('  其他非流动资产', [22283, 27979, 32172, 36423, 41307]),
    19: ('非流动资产合计', 'formula'),
    20: ('', None),
    21: ('资产总计', 'formula'),
    22: ('', None),
    # 负债
    23: ('负债及股东权益', None),
    24: ('流动负债', None),
    25: ('  应付账款', [16377, 53730, 60039, 62833, 65844]),
    26: ('  应计费用', None),
    27: ('  递延收入', None),
    28: ('  短期债务', None),
    29: ('  其他流动负债', [42967, 47763, 59279, 64845, 69031]),
    30: ('流动负债合计', 'formula'),
    31: ('', None),
    32: ('非流动负债', None),
    33: ('  长期债务', [98661, 124719, 120069, 111088, 99028]),
    34: ('  递延所得税负债', None),
    35: ('  其他非流动负债', None),
    36: ('非流动负债合计', 'formula'),
    37: ('', None),
    38: ('负债合计', 'formula'),
    39: ('', None),
    # 股东权益
    40: ('股东权益', None),
    41: ('  普通股', [50779, 57365, 64849, 73181, 83779]),
    42: ('  留存收益', [14933, 15157, -3068, -14050, -15545]),
    43: ('  累计其他综合收益', None),
    44: ('股东权益合计', 'formula'),
    45: ('', None),
    46: ('负债及股东权益总计', 'formula'),
}

for row_num, (item, values) in bs_structure.items():
    ws_bs.cell(row=row_num, column=1).value = item

    if values == 'formula':
        if row_num == 12:  # 流动资产合计
            for col in range(2, 12):
                col_letter = get_column_letter(col)
                ws_bs.cell(row=row_num, column=col).value = f'=SUM({col_letter}7:{col_letter}11)'
        elif row_num == 19:  # 非流动资产合计
            for col in range(2, 12):
                col_letter = get_column_letter(col)
                ws_bs.cell(row=row_num, column=col).value = f'=SUM({col_letter}15:{col_letter}18)'
        elif row_num == 21:  # 资产总计
            for col in range(2, 12):
                col_letter = get_column_letter(col)
                ws_bs.cell(row=row_num, column=col).value = f'={col_letter}12+{col_letter}19'
        elif row_num == 30:  # 流动负债合计
            for col in range(2, 12):
                col_letter = get_column_letter(col)
                ws_bs.cell(row=row_num, column=col).value = f'=SUM({col_letter}25:{col_letter}29)'
        elif row_num == 36:  # 非流动负债合计
            for col in range(2, 12):
                col_letter = get_column_letter(col)
                ws_bs.cell(row=row_num, column=col).value = f'=SUM({col_letter}33:{col_letter}35)'
        elif row_num == 38:  # 负债合计
            for col in range(2, 12):
                col_letter = get_column_letter(col)
                ws_bs.cell(row=row_num, column=col).value = f'={col_letter}30+{col_letter}36'
        elif row_num == 44:  # 股东权益合计
            for col in range(2, 12):
                col_letter = get_column_letter(col)
                ws_bs.cell(row=row_num, column=col).value = f'=SUM({col_letter}41:{col_letter}43)'
        elif row_num == 46:  # 负债及股东权益总计
            for col in range(2, 12):
                col_letter = get_column_letter(col)
                ws_bs.cell(row=row_num, column=col).value = f'={col_letter}38+{col_letter}44'

    elif isinstance(values, list):
        for col_idx, value in enumerate(values):
            if value is not None:
                ws_bs.cell(row=row_num, column=col_idx+2).value = value
                ws_bs.cell(row=row_num, column=col_idx+2).font = input_font

# 预测应收账款 - 基于DSO
for col in range(7, 12):
    col_letter = get_column_letter(col)
    # DSO = AR / (Revenue/365)
    # AR = DSO * (Revenue/365)
    ws_bs.cell(row=9, column=col).value = f'=Assumptions!$B$13*(IS!{col_letter}5/365)'
    ws_bs.cell(row=9, column=col).font = formula_font

# 预测存货 - 基于DIO
for col in range(7, 12):
    col_letter = get_column_letter(col)
    ws_bs.cell(row=10, column=col).value = f'=Assumptions!$B$14*(IS!{col_letter}6/365)'
    ws_bs.cell(row=10, column=col).font = formula_font

# 预测应付账款 - 基于DPO
for col in range(7, 12):
    col_letter = get_column_letter(col)
    ws_bs.cell(row=25, column=col).value = f'=Assumptions!$B$15*(IS!{col_letter}6/365)'
    ws_bs.cell(row=25, column=col).font = formula_font

# 现金预测 - 简化处理，后续从CF链接
for col in range(7, 12):
    col_letter = get_column_letter(col)
    prev_col = get_column_letter(col - 1)
    ws_bs.cell(row=7, column=col).value = f'=CF!{col_letter}32'
    ws_bs.cell(row=7, column=col).font = Font(color='008000')  # 绿色 = 链接

# 其他资产负债表项目简化预测
for col in range(7, 12):
    col_letter = get_column_letter(col)
    prev_col = get_column_letter(col - 1)
    # 短期投资、其他流动资产保持
    ws_bs.cell(row=8, column=col).value = f'={prev_col}8'
    ws_bs.cell(row=11, column=col).value = f'={prev_col}11'
    ws_bs.cell(row=15, column=col).value = f'={prev_col}15'
    ws_bs.cell(row=16, column=col).value = f'={prev_col}16'
    ws_bs.cell(row=18, column=col).value = f'={prev_col}18'
    ws_bs.cell(row=29, column=col).value = f'={prev_col}29'
    ws_bs.cell(row=33, column=col).value = f'={prev_col}33'

ws_bs.column_dimensions['A'].width = 35
for col in range(2, 12):
    ws_bs.column_dimensions[get_column_letter(col)].width = 12

print("✓ BS工作表完成")

# ========== CF 工作表 (现金流量表) ==========
ws_cf['A1'] = '苹果公司 (AAPL) - 现金流量表'
ws_cf['A1'].font = Font(bold=True, size=16)
ws_cf['A2'] = '单位: 百万美元'
ws_cf['A2'].font = Font(italic=True)

# 列标题
ws_cf['A4'] = ''
for idx, year in enumerate(years):
    ws_cf.cell(row=4, column=idx+2).value = year
    ws_cf.cell(row=4, column=idx+2).fill = blue_fill
    ws_cf.cell(row=4, column=idx+2).font = header_font
    ws_cf.cell(row=4, column=idx+2).alignment = Alignment(horizontal='center')

# 现金流量表结构
cf_structure = {
    5: ('经营活动现金流', None),
    6: ('  净利润', 'link_is'),
    7: ('  折旧与摊销', [11056, 11105, 11112, 11544, 11283]),
    8: ('  股权激励费用', [6832, 9084, 9038, 10582, 11989]),
    9: ('  营运资本变动', None),
    10: ('    应收账款变动', None),
    11: ('    存货变动', None),
    12: ('    应付账款变动', None),
    13: ('  其他经营性项目变动', [9722, 15908, 24724, 19200, 15620]),
    14: ('经营活动现金流合计', 'formula'),
    15: ('', None),
    16: ('投资活动现金流', None),
    17: ('  资本支出', [-7309, -11085, -10708, -10959, -9595]),
    18: ('  收购支出', None),
    19: ('  投资购买/(出售)', None),
    20: ('  其他投资活动', None),
    21: ('投资活动现金流合计', 'formula'),
    22: ('', None),
    23: ('筹资活动现金流', None),
    24: ('  债务发行(偿还)', None),
    25: ('  股权回购', None),
    26: ('  股利支付', None),
    27: ('  其他筹资活动', None),
    28: ('筹资活动现金流合计', 'formula'),
    29: ('', None),
    30: ('现金变动净额', 'formula'),
    31: ('  期初现金余额', None),
    32: ('  期末现金余额', 'formula'),
}

for row_num, (item, values) in cf_structure.items():
    ws_cf.cell(row=row_num, column=1).value = item

    if values == 'link_is':
        # 链接到利润表净利润
        for col in range(2, 12):
            col_letter = get_column_letter(col)
            ws_cf.cell(row=row_num, column=col).value = f'=IS!{col_letter}21'
            ws_cf.cell(row=row_num, column=col).font = Font(color='008000')

    elif values == 'formula':
        if row_num == 14:  # 经营活动现金流合计
            for col in range(2, 12):
                col_letter = get_column_letter(col)
                ws_cf.cell(row=row_num, column=col).value = f'=SUM({col_letter}6:{col_letter}13)'
        elif row_num == 21:  # 投资活动现金流合计
            for col in range(2, 12):
                col_letter = get_column_letter(col)
                ws_cf.cell(row=row_num, column=col).value = f'=SUM({col_letter}17:{col_letter}20)'
        elif row_num == 28:  # 筹资活动现金流合计
            for col in range(2, 12):
                col_letter = get_column_letter(col)
                ws_cf.cell(row=row_num, column=col).value = f'=SUM({col_letter}24:{col_letter}27)'
        elif row_num == 30:  # 现金变动净额
            for col in range(2, 12):
                col_letter = get_column_letter(col)
                ws_cf.cell(row=row_num, column=col).value = f'={col_letter}14+{col_letter}21+{col_letter}28'
        elif row_num == 32:  # 期末现金余额
            for col in range(2, 12):
                col_letter = get_column_letter(col)
                ws_cf.cell(row=row_num, column=col).value = f'={col_letter}30+{col_letter}31'

    elif isinstance(values, list):
        for col_idx, value in enumerate(values):
            if value is not None:
                ws_cf.cell(row=row_num, column=col_idx+2).value = value
                ws_cf.cell(row=row_num, column=col_idx+2).font = input_font

# 营运资本变动公式
for col in range(2, 12):
    col_letter = get_column_letter(col)
    # 应收账款变动 (增加为负，减少为正)
    if col > 2:
        prev_col = get_column_letter(col - 1)
        ws_cf.cell(row=10, column=col).value = f'=-({col_letter}9-{prev_col}9)'
        ws_cf.cell(row=11, column=col).value = f'=-({col_letter}10-{prev_col}10)'
        ws_cf.cell(row=12, column=col).value = f'={col_letter}25-{get_column_letter(col-1)}25'

# 期初现金余额
ws_cf.cell(row=31, column=2).value = 38016  # FY2020期初
ws_cf.cell(row=31, column=2).font = input_font
for col in range(3, 12):
    prev_col = get_column_letter(col - 1)
    ws_cf.cell(row=31, column=col).value = f'={prev_col}32'

# 预测折旧
for col in range(7, 12):
    col_letter = get_column_letter(col)
    prev_col = get_column_letter(col - 1)
    ws_cf.cell(row=7, column=col).value = f'={prev_col}7'
    ws_cf.cell(row=8, column=col).value = f'={prev_col}8'

# 预测资本支出
for col in range(7, 12):
    col_letter = get_column_letter(col)
    ws_cf.cell(row=17, column=col).value = f'=-IS!{col_letter}5*Assumptions!$B$21'
    ws_cf.cell(row=17, column=col).font = formula_font

# 简化其他项目预测
for col in range(7, 12):
    col_letter = get_column_letter(col)
    prev_col = get_column_letter(col - 1)
    ws_cf.cell(row=13, column=col).value = f'={prev_col}13'

ws_cf.column_dimensions['A'].width = 35
for col in range(2, 12):
    ws_cf.column_dimensions[get_column_letter(col)].width = 12

print("✓ CF工作表完成")

# ========== Checks 工作表 ==========
ws_checks['A1'] = '模型验证检查'
ws_checks['A1'].font = Font(bold=True, size=16)

ws_checks['A3'] = '检查项目'
ws_checks['B3'] = 'FY2024A'
ws_checks['C3'] = '状态'
ws_checks['D3'] = '说明'
for col in range(1, 5):
    ws_checks.cell(row=3, column=col).fill = blue_fill
    ws_checks.cell(row=3, column=col).font = header_font

checks = [
    ('资产负债表平衡', '=BS!F21-BS!F46', '=IF(ABS(B4)<1,"✓ 通过","✗ 失败")', '资产总计 = 负债及股东权益总计'),
    ('现金验证', '=CF!F32-BS!F7', '=IF(ABS(B5)<1,"✓ 通过","✗ 失败")', '现金流期末现金 = 资产负债表现金'),
    ('净利润链接', '=IS!F21-CF!F6', '=IF(ABS(B6)<1,"✓ 通过","✗ 失败")', '利润表净利润 = 现金流净利润'),
]

row_num = 4
for check_name, formula, status, description in checks:
    ws_checks.cell(row=row_num, column=1).value = check_name
    ws_checks.cell(row=row_num, column=2).value = formula
    ws_checks.cell(row=row_num, column=3).value = status
    ws_checks.cell(row=row_num, column=4).value = description
    row_num += 1

ws_checks.column_dimensions['A'].width = 30
ws_checks.column_dimensions['B'].width = 15
ws_checks.column_dimensions['C'].width = 12
ws_checks.column_dimensions['D'].width = 40

print("✓ Checks工作表完成")

# 保存文件
output_file = 'apple_3_statement_model.xlsx'
wb.save(output_file)

print(f"\n{'='*60}")
print(f"✓ 苹果公司三表财务模型创建成功!")
print(f"{'='*60}")
print(f"文件名: {output_file}")
print(f"工作表: Assumptions, IS, BS, CF, Checks")
print(f"\n包含内容:")
print(f"  • 历史数据: FY2020A - FY2024A (5年)")
print(f"  • 预测期间: FY2025E - FY2029E (5年)")
print(f"  • 利润表: 收入、成本、费用、利润")
print(f"  • 资产负债表: 资产、负债、股东权益")
print(f"  • 现金流量表: 经营、投资、筹资活动")
print(f"  • 假设驱动: 收入增长、利润率、营运资本天数")
print(f"  • 自动链接: 三表自动关联")
print(f"  • 验证检查: 平衡检查、一致性验证")
print(f"{'='*60}")