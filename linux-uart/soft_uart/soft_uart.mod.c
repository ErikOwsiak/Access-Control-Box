#include <linux/module.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

MODULE_INFO(vermagic, VERMAGIC_STRING);
MODULE_INFO(name, KBUILD_MODNAME);

__visible struct module __this_module
__attribute__((section(".gnu.linkonce.this_module"))) = {
	.name = KBUILD_MODNAME,
	.init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
	.exit = cleanup_module,
#endif
	.arch = MODULE_ARCH_INIT,
};

#ifdef CONFIG_RETPOLINE
MODULE_INFO(retpoline, "Y");
#endif

static const struct modversion_info ____versions[]
__used
__attribute__((section("__versions"))) = {
	{ 0x143b3558, __VMLINUX_SYMBOL_STR(module_layout) },
	{ 0x3ce4ca6f, __VMLINUX_SYMBOL_STR(disable_irq) },
	{ 0xf9a482f9, __VMLINUX_SYMBOL_STR(msleep) },
	{ 0x22504427, __VMLINUX_SYMBOL_STR(param_ops_int) },
	{ 0x2e5810c6, __VMLINUX_SYMBOL_STR(__aeabi_unwind_cpp_pr1) },
	{ 0x4fef5657, __VMLINUX_SYMBOL_STR(hrtimer_active) },
	{ 0x714eef32, __VMLINUX_SYMBOL_STR(hrtimer_forward) },
	{ 0x472035d, __VMLINUX_SYMBOL_STR(hrtimer_cancel) },
	{ 0x47229b5c, __VMLINUX_SYMBOL_STR(gpio_request) },
	{ 0xdfa8d3e7, __VMLINUX_SYMBOL_STR(gpio_to_desc) },
	{ 0x7adeb8d4, __VMLINUX_SYMBOL_STR(ktime_get) },
	{ 0xb1ad28e0, __VMLINUX_SYMBOL_STR(__gnu_mcount_nc) },
	{ 0xc82df8f6, __VMLINUX_SYMBOL_STR(tty_register_driver) },
	{ 0x5fc262cb, __VMLINUX_SYMBOL_STR(mutex_unlock) },
	{ 0xf2bd21d1, __VMLINUX_SYMBOL_STR(put_tty_driver) },
	{ 0x7a820ff6, __VMLINUX_SYMBOL_STR(tty_set_operations) },
	{ 0x5c0b44ea, __VMLINUX_SYMBOL_STR(hrtimer_start_range_ns) },
	{ 0x7ffc91fe, __VMLINUX_SYMBOL_STR(__tty_insert_flip_char) },
	{ 0x201a4b32, __VMLINUX_SYMBOL_STR(__mutex_init) },
	{ 0x27e1a049, __VMLINUX_SYMBOL_STR(printk) },
	{ 0xb410f71b, __VMLINUX_SYMBOL_STR(tty_port_init) },
	{ 0x195a71c2, __VMLINUX_SYMBOL_STR(mutex_lock) },
	{ 0x1a98b296, __VMLINUX_SYMBOL_STR(gpiod_direction_input) },
	{ 0x505fff58, __VMLINUX_SYMBOL_STR(gpiod_direction_output_raw) },
	{ 0xd6b8e852, __VMLINUX_SYMBOL_STR(request_threaded_irq) },
	{ 0x2196324, __VMLINUX_SYMBOL_STR(__aeabi_idiv) },
	{ 0xda4980d9, __VMLINUX_SYMBOL_STR(gpiod_set_debounce) },
	{ 0x67b27ec1, __VMLINUX_SYMBOL_STR(tty_std_termios) },
	{ 0xca58952e, __VMLINUX_SYMBOL_STR(tty_unregister_driver) },
	{ 0xa56344e3, __VMLINUX_SYMBOL_STR(__tty_alloc_driver) },
	{ 0xfe990052, __VMLINUX_SYMBOL_STR(gpio_free) },
	{ 0x409873e3, __VMLINUX_SYMBOL_STR(tty_termios_baud_rate) },
	{ 0xfcec0987, __VMLINUX_SYMBOL_STR(enable_irq) },
	{ 0xca7828b3, __VMLINUX_SYMBOL_STR(tty_port_link_device) },
	{ 0xd76f989, __VMLINUX_SYMBOL_STR(gpiod_to_irq) },
	{ 0x617f5b71, __VMLINUX_SYMBOL_STR(gpiod_set_raw_value) },
	{ 0x8be5575, __VMLINUX_SYMBOL_STR(hrtimer_init) },
	{ 0xaab60385, __VMLINUX_SYMBOL_STR(tty_flip_buffer_push) },
	{ 0x6c75d8dc, __VMLINUX_SYMBOL_STR(gpiod_get_raw_value) },
	{ 0xc1514a3b, __VMLINUX_SYMBOL_STR(free_irq) },
};

static const char __module_depends[]
__used
__attribute__((section(".modinfo"))) =
"depends=";


MODULE_INFO(srcversion, "FF97B9BF705FF2E8754580E");
