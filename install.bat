@echo off

xcopy . "%APPDATA%\Sublime Text 3\Packages\sublime-uroborosql-formatter\" /S/Y/Q
del "%APPDATA%\Sublime Text 3\Packages\sublime-uroborosql-formatter\install.bat"
del "%APPDATA%\Sublime Text 3\Packages\sublime-uroborosql-formatter\Readme.md"
del "%APPDATA%\Sublime Text 3\Packages\sublime-uroborosql-formatter\Readme.ja.md"

echo.
echo ##########################################################
echo Install Complete!!
echo.
echo Prease restart Sublime Text 3.
echo ##########################################################
echo.
pause