#!/bin/python
# Chuong trinh ket hop voi raw cho phep nguoi dung nhap vao

# Cach thu hien chuong trinh
#######################################
# python ex13_raw_input.py To Thanh
# Nhap doi so cua ban: Cong
#######################################

# KET QUA
########################################
# Ket qua la: To Thanh Cong
########################################

from sys import argv
ten_chuong_trinh, doiso1, doiso2 = argv
doi_so_nhap_vao = raw_input("Nhap doi so cua ban: ")
print "Ket qua la: %s %s %s" % (doiso1, doiso2, doi_so_nhap_vao)
