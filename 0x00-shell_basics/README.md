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
-> `[[:upper:]]*`: This is a pattern that matches any file or directory name starting with an uppercase letter. The square brackets **[ ]** indicate a character class, and **[:upper:]** is a predefined character class that matches uppercase letters.  
The * matches zero or more of any character after the uppercase letter.`/tmp/u:` This is the destination directory where the files and directories matching the pattern will be moved to. In this case, the destination directory is `/tmp/u`.
17. **101-clean_emacs** ==> Contains a script that deletes all files in the current working directory that end with the character ~  
**Solution brokedown**  
When you run the command rm `*\~`, the shell expands the `*\~` pattern to match all files in the current directory that end with a tilde (~) character. The resulting list of filenames is passed to the rm command, which then deletes each file.
18. **102-tree** ==> Contains a script that creates the directories `welcome/`, `welcome/to/` and `welcome/to/school` in the current directory.  
**Solution breakdown**  
The `-p` option allows you to create parent directories as needed, meaning that if the parent directories of a specified directory do not exist, they will be created as well.  
Incase there is need to ovewrite the existent files, we can consider using the `-f` option.  
19. **103-commas** ==> The `ls` command is used to list the contents of a directory in a Linux/Unix system. By default, running the command ls will display the names of the files and directories in the current directory.  
**Common options that can be used with the ls command**
	* `-a`: Shows hidden files (files that start with a dot).
	* `-A`: Shows all files except . and ...
	* `-C`: Forces multi-column output, sorted vertically.
	* `-d`: Shows only directories themselves, not their contents.
	* `-F`: Appends a character to each file indicating its type (/ for directories, @ for symbolic links, | for FIFOs, = for sockets, and nothing for regular files).
	* `-h`: Makes file sizes "human-readable" (i.e. in a format like "5.2K" or "10M").
	* `-i`: Prints the inode number of each file.
	* `-l`: Shows files in long format, with details such as permissions, owner, group, size, and modification time.
	* `-m`: Lists the file names separated by commas.
	* `-n`: Shows numeric UIDs and GIDs instead of names.
	* `-o`: Same as -l, but without group information.
	* `-p`: Appends a forward slash (/) to directories.
	* `-q`: Shows non-printable characters as ?.
	* `-r`: Reverses the order of the sort.
	* `-R`: Shows subdirectories recursively.
	* `-s`: Shows file sizes in blocks (usually 1KB).
	* `-t`: Sorts by modification time, newest first.
	* `-u`: Sorts by access time, newest first.
	* `-U`: Shows files in unsorted order.
	* `-x`: Forces multi-column output, sorted horizontally.
	* `--color=[auto|always|never]`: Enables or disables colorized output.
	* `--full-time`: Shows modification times in full ISO format.
	* `--group-directories-first`: Puts directories before other files in the listing.
20. **school.mgc** ==> This file is used to detect School data files. **School data** files always contain the string **SCHOOL** at offset 0.  
**Solution breakdown**  
```0 string SCHOOL School data
!:mime School```  
We start by defining the offset, then declare the type we want to supply and the character set to look for **School**. We then provide the description that will be displayed when we trie to see all the files in the directory.  
`!:mime School` ==> The exclamation mark (!) indicates that this is a "magic" file header, and the ":mime" keyword specifies the MIME type associated with the file type. `School` defines the mime type of the document


## Summary
This project is aimed at creating ease of use of the linux system and also teach how to use the bash scripts.
