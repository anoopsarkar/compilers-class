	#.file	1 "catalan-int.c"
	.option pic2
	.section .rodata,0x1,0x2,0,8
	.section .text,0x1,0x6,4,4
	.section	.rodata

	.byte	0x24,0x52,0x65,0x76,0x69,0x73,0x69,0x6f
	.byte	0x6e,0x3a,0x20,0x31,0x2e,0x31,0x33,0x20
	.byte	0x24,0x0

	.byte	0x24,0x49,0x64,0x3a,0x20,0x73,0x74,0x61
	.byte	0x6e,0x64,0x61,0x72,0x64,0x73,0x2e,0x68
	.byte	0x2c,0x76,0x20,0x31,0x2e,0x32,0x32,0x20
	.byte	0x32,0x30,0x30,0x32,0x2f,0x30,0x38,0x2f
	.byte	0x30,0x37,0x20,0x31,0x34,0x3a,0x35,0x31
	.byte	0x3a,0x34,0x38,0x20,0x72,0x61,0x6a,0x69
	.byte	0x20,0x45,0x78,0x70,0x20,0x24,0x0

	.byte	0x24,0x52,0x65,0x76,0x69,0x73,0x69,0x6f
	.byte	0x6e,0x3a,0x20,0x31,0x2e,0x31,0x31,0x20
	.byte	0x24,0x0

	.byte	0x24,0x52,0x65,0x76,0x69,0x73,0x69,0x6f
	.byte	0x6e,0x3a,0x20,0x31,0x2e,0x31,0x33,0x20
	.byte	0x24,0x0

	.byte	0x24,0x52,0x65,0x76,0x69,0x73,0x69,0x6f
	.byte	0x6e,0x3a,0x20,0x31,0x2e,0x36,0x20,0x24
	.byte	0x0

	.byte	0x24,0x52,0x65,0x76,0x69,0x73,0x69,0x6f
	.byte	0x6e,0x3a,0x20,0x31,0x2e,0x32,0x20,0x24
	.byte	0x0
	.text
	.align	2
	.globl	fact
	.ent	fact
fact:
.LFB1:
	.frame	$fp,64,$31		# vars= 16, regs= 3/0, args= 0, extra= 16
	.mask	0xd0000000,-16
	.fmask	0x00000000,0
	subu	$sp,$sp,64
.LCFI0:
	sd	$31,48($sp)
.LCFI1:
	sd	$fp,40($sp)
.LCFI2:
	sd	$28,32($sp)
.LCFI3:
	move	$fp,$sp
.LCFI4:
	.set	noat
	lui	$1,%hi(%neg(%gp_rel(fact)))
	addiu	$1,$1,%lo(%neg(%gp_rel(fact)))
	daddu	$gp,$1,$25
	.set	at
	sw	$4,16($fp)
	lw	$2,16($fp)
	beq	$2,$0,.L2
	lw	$2,16($fp)
	addu	$2,$2,-1
	move	$4,$2
	la	$25,fact
	jal	$31,$25
	move	$3,$2
	lw	$2,16($fp)
	mult	$3,$2
	mflo	$4
	sw	$4,20($fp)
	b	.L3
.L2:
	li	$2,1			# 0x1
	sw	$2,20($fp)
.L3:
	lw	$2,20($fp)
	move	$sp,$fp
	ld	$31,48($sp)
	ld	$fp,40($sp)
	ld	$28,32($sp)
	addu	$sp,$sp,64
	j	$31
.LFE1:
	.end	fact
	.align	2
	.globl	choose
	.ent	choose
choose:
.LFB2:
	.frame	$fp,80,$31		# vars= 16, regs= 5/0, args= 0, extra= 16
	.mask	0xd0030000,-16
	.fmask	0x00000000,0
	subu	$sp,$sp,80
.LCFI5:
	sd	$31,64($sp)
.LCFI6:
	sd	$fp,56($sp)
.LCFI7:
	sd	$28,48($sp)
.LCFI8:
	sd	$17,40($sp)
.LCFI9:
	sd	$16,32($sp)
.LCFI10:
	move	$fp,$sp
.LCFI11:
	.set	noat
	lui	$1,%hi(%neg(%gp_rel(choose)))
	addiu	$1,$1,%lo(%neg(%gp_rel(choose)))
	daddu	$gp,$1,$25
	.set	at
	sw	$4,16($fp)
	sw	$5,20($fp)
	lw	$4,16($fp)
	la	$25,fact
	jal	$31,$25
	move	$16,$2
	lw	$4,20($fp)
	la	$25,fact
	jal	$31,$25
	move	$17,$2
	lw	$3,16($fp)
	lw	$2,20($fp)
	subu	$2,$3,$2
	move	$4,$2
	la	$25,fact
	jal	$31,$25
	mult	$17,$2
	mflo	$2
	div	$0,$16,$2
	mflo	$16
	.set	noreorder
	beql	$2,$0,1f
	break	7
1:
	.set	reorder
	move	$2,$16
	move	$sp,$fp
	ld	$31,64($sp)
	ld	$fp,56($sp)
	ld	$28,48($sp)
	ld	$17,40($sp)
	ld	$16,32($sp)
	addu	$sp,$sp,80
	j	$31
.LFE2:
	.end	choose
	.align	2
	.globl	catalan
	.ent	catalan
catalan:
.LFB3:
	.frame	$fp,64,$31		# vars= 16, regs= 3/0, args= 0, extra= 16
	.mask	0xd0000000,-16
	.fmask	0x00000000,0
	subu	$sp,$sp,64
.LCFI12:
	sd	$31,48($sp)
.LCFI13:
	sd	$fp,40($sp)
.LCFI14:
	sd	$28,32($sp)
.LCFI15:
	move	$fp,$sp
.LCFI16:
	.set	noat
	lui	$1,%hi(%neg(%gp_rel(catalan)))
	addiu	$1,$1,%lo(%neg(%gp_rel(catalan)))
	daddu	$gp,$1,$25
	.set	at
	sw	$4,16($fp)
	lw	$2,16($fp)
	sll	$2,$2,1
	move	$4,$2
	lw	$5,16($fp)
	la	$25,choose
	jal	$31,$25
	move	$3,$2
	lw	$2,16($fp)
	addu	$2,$2,1
	div	$0,$3,$2
	mflo	$3
	.set	noreorder
	beql	$2,$0,1f
	break	7
1:
	.set	reorder
	move	$2,$3
	move	$sp,$fp
	ld	$31,48($sp)
	ld	$fp,40($sp)
	ld	$28,32($sp)
	addu	$sp,$sp,64
	j	$31
.LFE3:
	.end	catalan
	.section	.rodata
	.align	3
.LC0:

	.byte	0x75,0x73,0x61,0x67,0x65,0x3a,0x20,0x63
	.byte	0x61,0x74,0x61,0x6c,0x61,0x6e,0x20,0x3c
	.byte	0x6e,0x75,0x6d,0x62,0x65,0x72,0x3e,0xa
	.byte	0x0
	.align	3
.LC1:

	.byte	0x63,0x61,0x74,0x61,0x6c,0x61,0x6e,0x3a
	.byte	0x20,0x25,0x64,0x20,0x25,0x64,0xa,0x0
	.text
	.align	2
	.globl	main
	.ent	main
main:
.LFB4:
	.frame	$fp,64,$31		# vars= 16, regs= 3/0, args= 0, extra= 16
	.mask	0xd0000000,-16
	.fmask	0x00000000,0
	subu	$sp,$sp,64
.LCFI17:
	sd	$31,48($sp)
.LCFI18:
	sd	$fp,40($sp)
.LCFI19:
	sd	$28,32($sp)
.LCFI20:
	move	$fp,$sp
.LCFI21:
	.set	noat
	lui	$1,%hi(%neg(%gp_rel(main)))
	addiu	$1,$1,%lo(%neg(%gp_rel(main)))
	daddu	$gp,$1,$25
	.set	at
	sw	$4,16($fp)
	sw	$5,20($fp)
	lw	$2,16($fp)
	slt	$2,$2,2
	beq	$2,$0,.L7
	la	$4,.LC0
	la	$25,printf
	jal	$31,$25
	li	$2,1			# 0x1
	sw	$2,28($fp)
	b	.L6
.L7:
	lw	$2,20($fp)
	addu	$2,$2,4
	lw	$4,0($2)
	move	$5,$0
	li	$6,10			# 0xa
	la	$25,strtol
	jal	$31,$25
	sw	$2,24($fp)
	lw	$4,24($fp)
	la	$25,catalan
	jal	$31,$25
	la	$4,.LC1
	lw	$5,24($fp)
	move	$6,$2
	la	$25,printf
	jal	$31,$25
	sw	$0,28($fp)
.L6:
	lw	$2,28($fp)
	move	$sp,$fp
	ld	$31,48($sp)
	ld	$fp,40($sp)
	ld	$28,32($sp)
	addu	$sp,$sp,64
	j	$31
.LFE4:
	.end	main
