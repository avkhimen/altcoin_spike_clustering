python3 get_data.py
unzip -o *.zip -d data/
rm *.zip
cd data/
rm *_1.csv
rm *_1440.csv
rm *_15.csv
rm *_720.csv
rm *_5.csv
rm *USD*
rm *CAD*
rm *AUD*
rm *EUR*
rm *JPY*
rm *GBP*
rm *CHF*
rm *AED*
rm *ETH_60.csv
rm *DAI_60.csv
rm *DOT_60.csv
cd ..
sleep 100000
python3 cluster_altcoins.py