# 0x17. Web stack debugging #3

## Objective
This project aims at impacting the skill of debuging of LAMP stacks.

## Requirements
1. strace ==> `sudo apt-get install strace`
2. tmux ==> `sudo apt-get install tmux`

#### tmux
tmux’s authors describe it as a terminal multiplexer. Behind this fancy term hides a simple concept: Within one terminal window you can open multiple windows and split-views (called “panes” in tmux lingo). Each pane will contain its own, independently running shell instance (bash, zsh, whatever you’re using). This allows you to have multiple terminal commands and applications running side by side without the need to open multiple terminal emulator windows.
tmux basically offers two main features:

1. Window management in your terminal
2. session management

#### strace
Strace is one of the most powerful process monitoring, diagnostic, instructional tool of Linux. It also acts as a debugging tool that helps in troubleshooting issues. It is majorly used for the following purposes:

1. Debugging Programs
2. Troubleshooting Programs
3. Intercept System calls by a process
4. Record system calls by a process
5. Signals received by a process
6. Trace running processes

## Special commands
### tmux
**Note:**=>Thus `C-b` simply means press the `Ctrl` and **b** keys at the same time  .
1. Sppliting panes ==> `C-b %`  
2. Navigating panes ==> `C-b <arrow key>`  
3. Closing Panes ==> `exit` or `Ctrl-d`  
4. Creating Window ==> `C-b c`  
5. Switching to Previous window ==> `C-b p`  
6. Switching to next window ==> `C-b n`  
7. Detaching current session ==> `C-b d`  
8. List current working sessions ==> `tmux ls`  
9. Connecting to a session ==> `tmux attach -t <session number>`  
**More** [tmux](https://www.hamvocke.com/blog/a-quick-and-easy-guide-to-tmux/)  

### strace
1. Apache status check ==> `service apache2 status`  
2. Check if port 80 is Listenning ==> `ss -tuna | grep 80`  
3. Check for Apache process PID ==> `lsof -i:80`  
4. Mornitor the Apache process using its PID ==> `strace -p <appache_process_PID>`  
**More** [strace](https://medium.com/@donjoedbest/how-i-resolved-an-http-500-error-with-tmux-and-strace-d429d46ebc79)

## Featured Files
1. **0-strace_is_your_friend.pp** ==> Contains Puppet code to solve errors found while useing **strace**

## Summary
Wordpress is a very popular tool, it allows you to run blogs, portfolios, e-commerce and company websites… It actually powers 26% of the web. Wordpress is usually run on LAMP (Linux, Apache, MySQL, and PHP), which is a very widely used set of tools.

The web stack being debuged is a Wordpress website running on a LAMP stack.
