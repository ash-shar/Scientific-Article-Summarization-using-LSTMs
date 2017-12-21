input_path=$1
output_path=$2

# input_path=../Sample_Data/Papers_Folder/
# output_path=../Sample_Data/Output/

python 1-parse_latex.py $input_path ${output_path}Papers_Out_1/
python 2-parse_text.py ${output_path}Papers_Out_1/ ${output_path}Papers_Out_2/ ${output_path}all-parsed-papers-category.txt
python 3-final_parser.py ${output_path}all-parsed-papers-category.txt ${output_path}Final_Output/