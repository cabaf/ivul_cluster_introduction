IDT_PATH="apps/idt"

source $IDT_PATH/enable.rc
$IDT_PATH/idt $1 | gzip > $2
