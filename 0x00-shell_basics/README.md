# 0x00. Shell, basics

## Objective
This project is aimed at revealing more on;
1. What the shell is
2. Navigation
3. Looking Around
4. Manipulating Files
5. Working with Commands

## Featured Commands
* cd
* ls
* pwd
* less
* file
* ln
* cp
* mv
* rm
* mkdir
* type
* which
* help
* man

## Featured files
1. **0-current_working_directory** ==> Contains the script that prints the absolute path name of the current working directory.  
2. **1-listit** ==> Contains the script that display the contents list of your current directory.  
3. **2-bring_me_home** ==> Contains the script that changes the working directory to the user’s home directory.  
4. **3-listfiles** ==> Contains the script that display current directory contents in a long format.  
5. **4-listmorefiles** ==> Contains the script that display current directory contents, including hidden files (starting with .). Use the long format.  
6. **5-listfilesdigitonly** ==> Contains the script that display current directory contents.  
7. **6-firstdirectory** ==> Contains a script that creates a directory named my_first_directory in the `/tmp/` directory.  
8. **7-movethatfile** ==> Contains a script that moves the file betty from `/tmp/` to `/tmp/my_first_directory`.  
9. **8-firstdelete** ==> Contains a script that deletes the file `betty`.
10. **9-firstdirdeletion** ==> Contains a script that deletes the directory `my_first_directory` that is in the `/tmp` directory.  
11. **10-back** ==> Contains a script that changes the working directory to the previous one.
12. **11-lists** ==> Contains a script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.  
**Take Away(T.A)**
	* **Filtering of files** => ls -la | grep "^-"
	* **folow list format** ==> ls -`f`la or ls -la . .. /boot
13. **12-file_type** ==> contains a script that prints the type of the file named `iamafile`, which is in the `/tmp`.  
**Take Away(T.A)**
	* **file** ==> In Linux, the file command is a command-line utility that is used to determine the type of a file. It examines the contents of a file and tries to identify what kind of data it contains.
14. **13-symbolic_link** ==> Contains a script that creates a symbolic link to `/bin/ls`, named `__ls__`. The symbolic link created the current working directory.  
**Take Away(T.A)**
	* **ln** ==> In Linux, the ln command is used to create links between files. It can create either hard links or symbolic links. The syntax for the `ln` command is as follows: `ln [OPTIONS] <SOURCE> <DESTINATION>`.  
	**Examples**  
		* `ln -i file1 link1`
		This will create a **hard link** called **link1** to the file **file1**. If you modify either **file1** or **link1**, the changes will be reflected in both files because they point to the same data on the disk.
		* `ln -s file1 link1`
		This will create a **symbolic link** called **link1** to the file **file1**. If you modify **file1**, the changes will be reflected in **link1**. However, if you modify **link1**, the changes will not affect **file1**.
15. **14-copy_html** ==> Contians a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.  
**Take Away(T.A)**
	* **cp** ==> In Linux, the cp command is used to copy files or directories from one location to another. The basic syntax for the cp command is as follows: `cp [OPTIONS] <SOURCE> <DESTINATION>`
	**Examples**
		* `cp file1 folder1/`
		Copies a file named **file1** from the current directory to a directory called **folder1**  
**Commonly used options**
	* `-i` (interactive) ==> prompts before overwriting existing files
	* `-r` (recursive): copies directories and their contents recursively
	* `-p` (preserve): preserves file attributes such as permissions, timestamps, and ownership
	* `-a` (archive): preserves file attributes and copies recursively, equivalent to -p -r
	* `-f` (force): forces overwrite of existing files without prompting
	* `-u` (update): copies only when the source file is newer than the destination file, or the destination file does not exist
	* `-v` (verbose): prints the name of each file as it is copied
	* `-n` (no-clobber): does not overwrite existing files, equivalent to -i -n
16. **100-lets_move** ==> Contains a script that moves all files beginning with an uppercase letter to the directory **/tmp/u**
**Take Away(T.A)**
	* **mv** ==> In Linux, the mv command is used to move or rename files and directories. Here's the basic syntax of the mv command: `mv [options] source_file(s) destination`
	**Example**
		* **Move a file to a directory** ==> `mv file.txt /home/user/documents/`
		* **Rename a file** ==> `mv oldname.txt newname.txt`
		* **Move multiple files to a directory** ==> `mv file1.txt file2.txt /home/user/documents/`
		* **Move a directory** ==> `mv directory1 /home/user/documents/`
**Character Class** ==> In Linux and other Unix-like systems, a character class is a set of characters that can be used to match a single character in a pattern. Character classes are used in various commands and utilities that work with patterns, such as regular expressions and file globbing.  
**Some of the main Character classes include;**
* `[:alnum:]` - matches any alphanumeric character
* `[:alpha:]` - matches any alphabetic character
* `[:blank:]` - matches any horizontal whitespace character, including space and tab
* `[:cntrl:]` - matches any control character
* `[:digit:]` - matches any digit (0-9)
* `[:graph:]` - matches any printable character except space
* `[:lower:]` - matches any lowercase letter
* `[:print:]` - matches any printable character, including space
* `[:punct:]` - matches any punctuation character
* `[:space:]` - matches any whitespace character, including space, tab, and newline
* `[:upper:]` - matches any uppercase letter
* `[:xdigit:]` - matches any hexadecimal digit (0-9, A-F, a-f)  
**Solution brokedown**  
`mv [[:upper:]]* /tmp/u`  
-> `mv`: This is the command for "move".  
-> `[[:upper:]]*`: This is a pattern that matches any file or directory name starting with an uppercase letter. The square brackets **[ ]** indicate a character class, and **[:upper:]** is a predefined character class that matches uppercase letters. The** * **matches zero or more of any character after the uppercase letter.`/tmp/u:` This is the destination directory where the files and directories matching the pattern will be moved to. In this case, the destination directory is `/tmp/u`.


## Summary
This project is aimed at creating ease of use of the linux system and also teach how to use the bash scripts.
