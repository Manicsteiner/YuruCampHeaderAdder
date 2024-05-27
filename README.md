# YuruCampHeaderAdder
Image tool for game "Yuru Camp Have a nice day"&amp;"Summertime Render Another Horizon" (Switch)
Those pictures are DDS files without header, just add a header to it is okay.
Script will identify dimensions of a texture from original file's footer.

For BG and EG use following command:
```
python headeradder.py "path/to/file1" "path/to/file2" ...
```

For SP, BU and MG (STRAH only) use following command:
```
python headeradder.py -alpha "path/to/file1" "path/to/file2" ...
```
