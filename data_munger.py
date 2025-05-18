# data_munger.py
# 该脚本用于提取原始销售数据中关于 Pink Morsel 的交易记录，并生成结构化的 CSV 文件供分析使用

import csv
import os

# 输入数据所在目录
DATA_DIRECTORY = "./data"

# 输出文件路径
OUTPUT_FILE_PATH = "./formatted_data.csv"

# 打开输出文件以写入格式化数据
with open(OUTPUT_FILE_PATH, "w") as output_file:
    writer = csv.writer(output_file)

    # 写入 CSV 文件表头
    header = ["sales", "date", "region"]
    writer.writerow(header)

    # 遍历数据目录下所有 CSV 文件
    for file_name in os.listdir(DATA_DIRECTORY):
        # 打开每个文件进行读取
        with open(f"{DATA_DIRECTORY}/{file_name}", "r") as input_file:
            reader = csv.reader(input_file)
            row_index = 0

            # 遍历每一行
            for input_row in reader:
                # 跳过第一行表头
                if row_index > 0:
                    product = input_row[0]
                    raw_price = input_row[1]
                    quantity = input_row[2]
                    transaction_date = input_row[3]
                    region = input_row[4]

                    # 只处理 pink morsel 的记录
                    if product == "pink morsel":
                        # 去掉 $ 符号，并转换为浮点数
                        price = float(raw_price[1:])
                        # 计算该行销售额
                        sale = price * int(quantity)

                        # 写入结构化数据行
                        output_row = [sale, transaction_date, region]
                        writer.writerow(output_row)
                row_index += 1
