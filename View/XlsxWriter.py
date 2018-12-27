import xlsxwriter
from calendar import monthrange
from View import DBManager

col_name_ZH = ['序号', '日期', '产品名称', '重量（吨）', '单价（元/吨）', '金额（元）', '车辆号码', '备注']
TITLE_ROW = 5
CONTENT_START_ROW = TITLE_ROW + 1


def sort_by_date(order):
    return order[2]


def export(data, year_month, customer):
    billing_info_raw = []
    with open('secret.txt', 'r') as file:
        for line in file:
            billing_info_raw.append(line)

    billing_info = []
    for i in billing_info_raw:

        billing_info.append(i.replace('\n', '').split("-"))
    print(billing_info)



    for i in range(0, len(year_month)):
        year_month[i] = int(year_month[i])

    workbook = xlsxwriter.Workbook(f'{customer}结算单.xlsx')
    worksheet = workbook.add_worksheet()

    worksheet.set_paper(9)

    title_format = workbook.add_format({
        'font_size': 20,
        'align': 'center',
        'valign': 'vcenter',
    })
    title_date_format = workbook.add_format({
        'font_size': 12,
        'align': 'center',
        'valign': 'vcenter',
    })
    content_format_wb_align = workbook.add_format({
        'font_size': 12,
        'align': 'center',
        'valign': 'vcenter',
        'border': 1
    })
    content_format_nb = workbook.add_format({
        'font_size': 12,
    })
    content_format_ltb = workbook.add_format({
        'font_size': 12,
        'top': 1,
        'left': 1,
        'bottom': 1
    })
    content_format_tb = workbook.add_format({
        'font_size': 12,
        'top': 1,
        'bottom': 1
    })
    content_format_tbr = workbook.add_format({
        'font_size': 12,
        'top': 1,
        'bottom': 1,
        'right': 1,
        'underline': 1,
        'align': 'center',
        'valign': 'vcenter'
    })
    content_format_tbr.set_num_format('#,##0.00')
    content_format_wb = workbook.add_format({
        'font_size': 12,
        'border': 1
    })

    worksheet.set_column(0, 0, 5)
    worksheet.set_column(1, 1, 15)
    worksheet.set_column(2, 2, 15)
    worksheet.set_column(3, 3, 11)
    worksheet.set_column(4, 4, 11)
    worksheet.set_column(5, 5, 11)
    worksheet.set_column(6, 6, 12)
    worksheet.set_column(7, 7, 15)

    worksheet.merge_range(0, 0, 0, 7, '结算单', title_format)
    worksheet.merge_range(1, 0, 1, 7, f'{year_month[0]}年{year_month[1]}月', title_date_format)
    worksheet.merge_range(2, 0, 2, 7, f'客户：{customer}', content_format_nb)
    worksheet.merge_range(3, 0, 3, 3, '您本月提货付款情况如下：')

    worksheet.merge_range(3, 4, 3, 7,
                          f'结算时间：{year_month[0]}年{year_month[1]}月1日' +
                          f'至{year_month[0]}年{year_month[1]}月{monthrange(year_month[0], year_month[1])[1]}日',
                          content_format_nb)

    worksheet.merge_range(4, 0, 4, 7, '提货明细：', content_format_nb)

    for i in range(0, 8):
        worksheet.write_string(TITLE_ROW, i, col_name_ZH[i], content_format_wb_align)

    data.sort(key=sort_by_date)

    line_counter = CONTENT_START_ROW
    index_counter = 1
    for i in data:
        date = str(i[0]) + '/' + str(i[1]) + '/' + str(i[2])
        worksheet.write(line_counter, 0, index_counter, content_format_wb)
        worksheet.write_string(line_counter, 1, date, content_format_wb)
        worksheet.write_string(line_counter, 2, i[4], content_format_wb)
        worksheet.write(line_counter, 3, i[6], content_format_wb)
        worksheet.write(line_counter, 4, i[7], content_format_wb)
        worksheet.write_formula(line_counter, 5, f'=D{1+line_counter}*E{1+line_counter}', content_format_wb)
        worksheet.write_string(line_counter, 6, i[3], content_format_wb_align)
        if i[8] == '无':
            worksheet.write_string(line_counter, 7, '', content_format_wb)
        else:
            worksheet.write_string(line_counter, 7, i[8], content_format_wb)
        line_counter += 1
        index_counter += 1
    worksheet.write_formula(line_counter, 3, f'=SUM(D{CONTENT_START_ROW + 1}:D{line_counter})', content_format_wb)
    worksheet.write_string(line_counter, 4, '', content_format_wb)
    worksheet.write_formula(line_counter, 5, f'=SUM(F{CONTENT_START_ROW+1}:F{line_counter})', content_format_wb)
    worksheet.write_string(line_counter, 6, '', content_format_wb)
    worksheet.write_string(line_counter, 7, '', content_format_wb)
    worksheet.merge_range(line_counter, 0, line_counter, 2, '合计', content_format_wb_align)
    line_counter += 1
    worksheet.merge_range(line_counter, 0, line_counter, 2, '本期货款: 大写人民币', content_format_ltb)
    worksheet.merge_range(line_counter, 3, line_counter, 5, f'''=SUBSTITUTE(SUBSTITUTE(TEXT(INT(F{line_counter}),
        "[DBNum2][$-804]G/通用格式元"&IF(INT(F{line_counter})=F{line_counter},"整",""))&TEXT(MID(F{line_counter},FIND("."
        ,F{line_counter}&".0")+1,1),"[DBNum2][$-804]G/通用格式角")&TEXT(MID(F{line_counter},FIND(".",F{line_counter}&".0
        ")+2,1),"[DBNum2][$-804]G/通用格式分"),"零角","零"),"零分","")''', content_format_tb)
    worksheet.merge_range(line_counter, 6, line_counter, 7, f'="¥"&F{line_counter - 1}', content_format_tbr)
    line_counter += 1
    worksheet.merge_range(line_counter, 0, line_counter, 1, '付款情况', content_format_nb)
    line_counter += 1
    worksheet.merge_range(line_counter, 0, line_counter, 1, '上月末欠款', content_format_wb)
    worksheet.write(line_counter, 2, '', content_format_wb)
    line_counter += 1
    worksheet.merge_range(line_counter, 0, line_counter, 1, '本月货款', content_format_wb)
    worksheet.write(line_counter, 2, '', content_format_wb)
    line_counter += 1
    worksheet.merge_range(line_counter, 0, line_counter, 1, '本月收到货款', content_format_wb)
    worksheet.write(line_counter, 2, '', content_format_wb)
    line_counter += 1
    worksheet.merge_range(line_counter, 0, line_counter, 1, '本月末欠货款', content_format_wb)
    worksheet.write_formula(line_counter, 2, f'=C{line_counter-3}+C{line_counter-2}-C{line_counter-1}'
                            , content_format_wb)
    line_counter += 1
    worksheet.write_string(line_counter, 0, '以上货款双方核对无误， 请及时按月付清货款')
    line_counter += 1
    worksheet.write_string(line_counter, 0, f'收款户名： {billing_info[0][0]}')
    worksheet.write_string(line_counter, 4, f'收款户名： {billing_info[1][0]}')
    line_counter += 1
    worksheet.write_string(line_counter, 0, f'开户行： {billing_info[0][1]}')
    worksheet.write_string(line_counter, 4, f'开户行： {billing_info[1][1]}')
    line_counter += 1
    worksheet.write_string(line_counter, 0, f'卡号： {billing_info[0][2]}')
    worksheet.write_string(line_counter, 4, f'账号： {billing_info[1][2]}')
    line_counter += 1
    worksheet.write_string(line_counter, 0, '供货方')
    worksheet.write_string(line_counter, 4, '购货方')
    line_counter += 1
    worksheet.write_string(line_counter, 0, '经办人:')
    worksheet.write_string(line_counter, 4, '经办人:')
    line_counter += 2
    worksheet.merge_range(line_counter, 0, line_counter, 2, '_____年_____月_____日')
    worksheet.merge_range(line_counter, 4, line_counter, 5, '_____年_____月_____日')
    line_counter += 1
    workbook.close()


# if __name__ == '__main__':
#     # print(ord('A'))
#     # export([], ['2018', '12'], '客户名')
#     db_manager = DBManager.DatabaseManager()
#     db_manager.execute("SELECT * FROM orders where Month=11 AND YEAR=2018 AND Customer='福建六建集团有限公司（融侨观邸）'")
#     data = db_manager.fetch_all()
#     export(data, [2018, 12], '福建六建集团有限公司（融侨观邸）')



