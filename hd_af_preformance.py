import pandas as pd
import sys

file_name = sys.argv[1]
file1 = pd.read_csv(file_name)
af_block_value = file1[~file1["blocked_reason"].isnull()]["blocked_reason"].value_counts()
af_block_names = af_block_value.keys().tolist()
hd_block_value = file1[~file1["anti_type"].isnull()]["anti_type"].value_counts()
hd_block_names = hd_block_value.keys().tolist()


str1 = " \t \t %s\r\n" % ("\t".join(af_block_names))
str2 = " \t \t %s\r\n" % ("\t".join([str(i) for i in af_block_value.tolist()]))

with open("af_hd_result.csv","w") as f:
    f.write(str1)
    f.write(str2)
    for each_hd in hd_block_names:
        str3 = "%s\t%d" % (each_hd,hd_block_value[each_hd])
        mlist = []
        for each_af in af_block_names:
            join_result = sum((file1["anti_type"] == each_hd)&(file1['blocked_reason'] == each_af))
            mlist.append(join_result)
        str3 = "%s\t%s\r\n" % (str3,"\t".join([str(i) for i in mlist]))
        f.write(str3)
