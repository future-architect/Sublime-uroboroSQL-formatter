@echo off

xcopy .\* "%APPDATA%\Sublime Text 3\Packages\sublime-uroborosql-formatter" /I/D/Y/Q
xcopy .\yaml "%APPDATA%\Sublime Text 3\Packages\sublime-uroborosql-formatter\yaml" /I/D/Y/Q
del "%APPDATA%\Sublime Text 3\Packages\sublime-uroborosql-formatter\install.bat"
del "%APPDATA%\Sublime Text 3\Packages\sublime-uroborosql-formatter\Readme.md"

echo.
echo ##########################################################
echo Install Complete!!
echo.
echo sublime-uroborosql-formatterのインストールが完了しました。
echo Sublime Text 3を再起動してください。
echo ##########################################################
echo.
pause