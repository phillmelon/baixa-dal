#!/bin/bash
echo $(date -d "today" +"%Y.%m.%d.%H%M")
mkdir $(date -d "today" +"%Y.%m.%d.%H%M")
cd $(date -d "today" +"%Y.%m.%d.%H%M")

#https://docs.google.com/spreadsheets/d/1S7qHMUV8fDfpEx9nUQ_oIaTJLLxPZAPIm8NVq3VN0zs/edit#gid=360701187
#wget --output-file="rgl.log" "https://docs.google.com/spreadsheets/d/1S7qHMUV8fDfpEx9nUQ_oIaTJLLxPZAPIm8NVq3VN0zs/export?format=xlsx&gid=360701187" -O "rgl.xlsx"
wget "https://docs.google.com/spreadsheets/d/1S7qHMUV8fDfpEx9nUQ_oIaTJLLxPZAPIm8NVq3VN0zs/export?format=xlsx" -O "rgl.xlsx"
wget "https://docs.google.com/spreadsheets/d/1S7qHMUV8fDfpEx9nUQ_oIaTJLLxPZAPIm8NVq3VN0zs/export?format=pdf" -O "rgl.pdf"

#https://docs.google.com/spreadsheets/d/1crFlTaoDEXXFu5WN69myv2yhhaRpV8Hy4_s8ZZMYKWA/edit?folder=19AhdZbiFTLgki6Mb5lpH8OWjl651iENy#gid=1005409188
#wget --output-file="expediente-dal.log" "https://docs.google.com/spreadsheets/d/1crFlTaoDEXXFu5WN69myv2yhhaRpV8Hy4_s8ZZMYKWA/export?format=xlsx&gid=1005409188" -O "expediente-dal.xlsx"
wget "https://docs.google.com/spreadsheets/d/1crFlTaoDEXXFu5WN69myv2yhhaRpV8Hy4_s8ZZMYKWA/export?format=xlsx" -O "expediente-dal.xlsx"
wget "https://docs.google.com/spreadsheets/d/1crFlTaoDEXXFu5WN69myv2yhhaRpV8Hy4_s8ZZMYKWA/export?format=pdf" -O "expediente-dal.pdf"

#https://docs.google.com/spreadsheets/d/1AfBFjNogHbMDlTSHRKq-R9B_184K_k9gN_xzcg2ESaQ/edit#gid=931140496
#wget --output-file="autografos-e-prazos.log" "https://docs.google.com/spreadsheets/d/1AfBFjNogHbMDlTSHRKq-R9B_184K_k9gN_xzcg2ESaQ/export?format=xlsx&gid=931140496" -O "autografos-e-prazos.xlsx"
wget "https://docs.google.com/spreadsheets/d/1AfBFjNogHbMDlTSHRKq-R9B_184K_k9gN_xzcg2ESaQ/export?format=xlsx" -O "autografos-e-prazos.xlsx"
wget "https://docs.google.com/spreadsheets/d/1AfBFjNogHbMDlTSHRKq-R9B_184K_k9gN_xzcg2ESaQ/export?format=pdf" -O "autografos-e-prazos.pdf"

#https://docs.google.com/spreadsheets/d/1J8eZfiyVFvFByBwxUMpeS0_l3IRoSTvWp-x3FDeTTXc/edit#gid=573190444
#wget --output-file="pareceres-das-comissoes.log" "https://docs.google.com/spreadsheets/d/1J8eZfiyVFvFByBwxUMpeS0_l3IRoSTvWp-x3FDeTTXc/export?format=xlsx&gid=573190444" -O "pareceres-das-comissoes.xlsx"
wget "https://docs.google.com/spreadsheets/d/1J8eZfiyVFvFByBwxUMpeS0_l3IRoSTvWp-x3FDeTTXc/export?format=xlsx" -O "pareceres-das-comissoes.xlsx"
wget "https://docs.google.com/spreadsheets/d/1J8eZfiyVFvFByBwxUMpeS0_l3IRoSTvWp-x3FDeTTXc/export?format=pdf" -O "pareceres-das-comissoes.pdf"

#https://docs.google.com/spreadsheets/d/187faD_rvGeckyyCrhKq1gFMGaYkPIf8j0AAUIGtWMKw/edit#gid=324485490
wget "https://docs.google.com/spreadsheets/d/187faD_rvGeckyyCrhKq1gFMGaYkPIf8j0AAUIGtWMKw/export?format=xlsx" -O "ri.xlsx"
wget "https://docs.google.com/spreadsheets/d/187faD_rvGeckyyCrhKq1gFMGaYkPIf8j0AAUIGtWMKw/export?format=pdf" -O "ri.pdf"
#wget "https://docs.google.com/spreadsheets/d/1S7qHMUV8fDfpEx9nUQ_oIaTJLLxPZAPIm8NVq3VN0zs/export?format=xlsx&gid=360701187" -O ".xlsx"

cd ..

echo "Done."