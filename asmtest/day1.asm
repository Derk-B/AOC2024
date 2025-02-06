%define STDIN 0
%define STDOUT 1
%define STDERR 2

%define READ 0
%define WRITE 1
%define OPEN 2
%define CLOSE 3

	global _start
	
	section .data
filename: db "aoc.txt", 0

score: dq 0
result: db "Result: %d", 10, 0
debugNumber: db "Current: %d", 10, 0

error_file_open: db "Could not open file"
error_file_open_len: equ $-error_file_open
	
	section .bss
input: resb 7000

	section .text
	extern printf
	extern putchar
_start: 
	; Open file input.txt
	mov rax, OPEN
	mov rdi, filename
	mov rsi, 0 ; read-only mode
	syscall

	cmp rax, 0
	js file_open_error
	mov rbx, rax

	; Read first 4kB from file
	mov rax, READ 
	mov rdi, rbx
	mov rsi, input
	mov rdx, 4096
	syscall

	; Read remaining from file
	mov rax, READ 
	mov rdi, rbx
	lea rsi, [input+4096]
	mov rdx, 2904
	syscall

	; Close file input.txt
	mov rax, CLOSE
	mov rdi, rbx
	syscall

	mov rcx, 7000 ; rcx contains the total length of the input
	mov rsi, input

count_input:
	cmp rcx, 0 ; If end of buffer was reached
	je print_result

	mov al, byte [rsi]
	cmp al, 40
	jne decrement_score

increment_score:
	mov rax, [score]
	inc rax
	mov [score], rax
	jmp next_iter

decrement_score:
	mov rax, [score]
	dec rax,
	mov [score], rax

next_iter:
	inc rsi

	dec rcx
	jmp count_input



print_result:
	mov rdi, result
	mov rsi, [score]
	xor rax, rax
	call printf

	jmp exit_program

file_open_error:
	mov rax, WRITE
	mov rdi, STDOUT
	mov rsi, error_file_open
	mov rdx, error_file_open_len
	syscall

exit_program:
	mov rax, 60
	xor rdi, rdi
	syscall
