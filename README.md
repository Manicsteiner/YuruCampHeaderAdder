# YuruCampHeaderAdder
Image tool for game "_Yuru Camp Have a nice day_"&amp;"_Summertime Render Another Horizon_" (Switch platform)  

First, find a way to get a copy of the game and use some tools to extract it (such as a configured emulator). Then, find some CPK files in romfs\StreamingAssets\1920x1080, use [GARbro](https://github.com/crskycode/GARbro) or vgmtoolbox to extract it and get some files without extension name.  
Those files are DDS picture files without header, just add a header to it is okay.  
Script will identify dimensions of a texture from original file's footer.  

For BG and EG, or let script recognize its format, just drag and drop files on script, or use following command:  
```
python headeradder.py "path/to/file1" "path/to/file2" ...
```

For SP, BU and MG (STRAH only) use following command:  
```
python headeradder.py -alpha "path/to/file1" "path/to/file2" ...
```
