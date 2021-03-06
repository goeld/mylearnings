@rem
@rem Copyright 2015 the original author or authors.
@rem
@rem Licensed under the Apache License, Version 2.0 (the "License");
@rem you may not use this file except in compliance with the License.
@rem You may obtain a copy of the License at
@rem
@rem      https://www.apache.org/licenses/LICENSE-2.0
@rem
@rem Unless required by applicable law or agreed to in writing, software
@rem distributed under the License is distributed on an "AS IS" BASIS,
@rem WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
@rem See the License for the specific language governing permissions and
@rem limitations under the License.
@rem

@if "%DEBUG%" == "" @echo off
@rem ##########################################################################
@rem
@rem  Web3App startup script for Windows
@rem
@rem ##########################################################################

@rem Set local scope for the variables with windows NT shell
if "%OS%"=="Windows_NT" setlocal

set DIRNAME=%~dp0
if "%DIRNAME%" == "" set DIRNAME=.
set APP_BASE_NAME=%~n0
set APP_HOME=%DIRNAME%..

@rem Add default JVM options here. You can also use JAVA_OPTS and WEB3_APP_OPTS to pass JVM options to this script.
set DEFAULT_JVM_OPTS=

@rem Find java.exe
if defined JAVA_HOME goto findJavaFromJavaHome

set JAVA_EXE=java.exe
%JAVA_EXE% -version >NUL 2>&1
if "%ERRORLEVEL%" == "0" goto init

echo.
echo ERROR: JAVA_HOME is not set and no 'java' command could be found in your PATH.
echo.
echo Please set the JAVA_HOME variable in your environment to match the
echo location of your Java installation.

goto fail

:findJavaFromJavaHome
set JAVA_HOME=%JAVA_HOME:"=%
set JAVA_EXE=%JAVA_HOME%/bin/java.exe

if exist "%JAVA_EXE%" goto init

echo.
echo ERROR: JAVA_HOME is set to an invalid directory: %JAVA_HOME%
echo.
echo Please set the JAVA_HOME variable in your environment to match the
echo location of your Java installation.

goto fail

:init
@rem Get command-line arguments, handling Windows variants

if not "%OS%" == "Windows_NT" goto win9xME_args

:win9xME_args
@rem Slurp the command line arguments.
set CMD_LINE_ARGS=
set _SKIP=2

:win9xME_args_slurp
if "x%~1" == "x" goto execute

set CMD_LINE_ARGS=%*

:execute
@rem Setup the command line

set CLASSPATH=%APP_HOME%\lib\Web3App-0.1.0.jar;%APP_HOME%\lib\web3j-unit-4.8.4.jar;%APP_HOME%\lib\web3j-evm-4.8.4.jar;%APP_HOME%\lib\core-4.8.4.jar;%APP_HOME%\lib\logback-classic-1.2.3.jar;%APP_HOME%\lib\logback-core-1.2.3.jar;%APP_HOME%\lib\logging-interceptor-4.9.0.jar;%APP_HOME%\lib\kotlin-stdlib-jdk8-1.4.10.jar;%APP_HOME%\lib\crypto-4.8.4.jar;%APP_HOME%\lib\abi-4.8.4.jar;%APP_HOME%\lib\tuples-4.8.4.jar;%APP_HOME%\lib\jnr-unixsocket-0.21.jar;%APP_HOME%\lib\okhttp-4.9.0.jar;%APP_HOME%\lib\rxjava-2.2.2.jar;%APP_HOME%\lib\Java-WebSocket-1.3.8.jar;%APP_HOME%\lib\jackson-databind-2.10.0.jar;%APP_HOME%\lib\testcontainers-1.15.1.jar;%APP_HOME%\lib\kotlin-logging-1.6.24.jar;%APP_HOME%\lib\log4j-to-slf4j-2.12.1.jar;%APP_HOME%\lib\docker-java-api-3.2.7.jar;%APP_HOME%\lib\docker-java-transport-zerodep-3.2.7.jar;%APP_HOME%\lib\slf4j-api-1.7.30.jar;%APP_HOME%\lib\junit-jupiter-engine-5.5.2.jar;%APP_HOME%\lib\junit-jupiter-params-5.5.2.jar;%APP_HOME%\lib\junit-jupiter-api-5.5.2.jar;%APP_HOME%\lib\guava-28.1-jre.jar;%APP_HOME%\lib\jackson-core-2.10.0.jar;%APP_HOME%\lib\jackson-annotations-2.10.3.jar;%APP_HOME%\lib\klaxon-5.0.1.jar;%APP_HOME%\lib\kotlin-reflect-1.3.61.jar;%APP_HOME%\lib\okio-2.8.0.jar;%APP_HOME%\lib\kotlin-stdlib-jdk7-1.4.10.jar;%APP_HOME%\lib\kotlin-stdlib-1.4.10.jar;%APP_HOME%\lib\rlp-4.8.4.jar;%APP_HOME%\lib\utils-4.8.4.jar;%APP_HOME%\lib\jnr-enxio-0.19.jar;%APP_HOME%\lib\jnr-posix-3.0.47.jar;%APP_HOME%\lib\jnr-ffi-2.1.9.jar;%APP_HOME%\lib\jnr-constants-0.9.11.jar;%APP_HOME%\lib\reactive-streams-1.0.2.jar;%APP_HOME%\lib\junit-4.12.jar;%APP_HOME%\lib\commons-compress-1.20.jar;%APP_HOME%\lib\duct-tape-1.0.8.jar;%APP_HOME%\lib\visible-assertions-2.1.2.jar;%APP_HOME%\lib\kotlin-logging-common-1.6.24.jar;%APP_HOME%\lib\junit-platform-engine-1.5.2.jar;%APP_HOME%\lib\junit-platform-commons-1.5.2.jar;%APP_HOME%\lib\apiguardian-api-1.1.0.jar;%APP_HOME%\lib\opentest4j-1.2.0.jar;%APP_HOME%\lib\log4j-api-2.12.1.jar;%APP_HOME%\lib\failureaccess-1.0.1.jar;%APP_HOME%\lib\listenablefuture-9999.0-empty-to-avoid-conflict-with-guava.jar;%APP_HOME%\lib\jsr305-3.0.2.jar;%APP_HOME%\lib\checker-qual-2.8.1.jar;%APP_HOME%\lib\error_prone_annotations-2.3.2.jar;%APP_HOME%\lib\j2objc-annotations-1.3.jar;%APP_HOME%\lib\animal-sniffer-annotations-1.18.jar;%APP_HOME%\lib\bcprov-jdk15on-1.65.jar;%APP_HOME%\lib\jffi-1.2.17.jar;%APP_HOME%\lib\jffi-1.2.17-native.jar;%APP_HOME%\lib\asm-commons-5.0.3.jar;%APP_HOME%\lib\asm-analysis-5.0.3.jar;%APP_HOME%\lib\asm-util-5.0.3.jar;%APP_HOME%\lib\asm-tree-5.0.3.jar;%APP_HOME%\lib\asm-5.0.3.jar;%APP_HOME%\lib\jnr-a64asm-1.0.0.jar;%APP_HOME%\lib\jnr-x86asm-1.0.2.jar;%APP_HOME%\lib\kotlin-stdlib-common-1.4.10.jar;%APP_HOME%\lib\annotations-13.0.jar;%APP_HOME%\lib\hamcrest-core-1.3.jar;%APP_HOME%\lib\jna-5.5.0.jar;%APP_HOME%\lib\docker-java-transport-3.2.7.jar

@rem Execute Web3App
"%JAVA_EXE%" %DEFAULT_JVM_OPTS% %JAVA_OPTS% %WEB3_APP_OPTS%  -classpath "%CLASSPATH%" org.web3j.Web3App %CMD_LINE_ARGS%

:end
@rem End local scope for the variables with windows NT shell
if "%ERRORLEVEL%"=="0" goto mainEnd

:fail
rem Set variable WEB3_APP_EXIT_CONSOLE if you need the _script_ return code instead of
rem the _cmd.exe /c_ return code!
if  not "" == "%WEB3_APP_EXIT_CONSOLE%" exit 1
exit /b 1

:mainEnd
if "%OS%"=="Windows_NT" endlocal

:omega
