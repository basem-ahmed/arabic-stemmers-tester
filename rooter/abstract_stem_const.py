﻿#!/usr/bin/python
# -*- coding=utf-8 -*-
"""
Constants used for stemming module
"""
from tashaphyne.stem_const import DEFAULT_PREFIX_LIST, DEFAULT_SUFFIX_LIST


VERB_PREFIX_LIST = (
    u"",
    u'ءأ',
    u'ا',
    u'ات',
    u'است',
    #~ u'ال',
    #~ u'الا',
    #~ u'الاست',
    #~ u'الان',
    #~ u'الأ',
    #~ u'الإ',
    #~ u'الت',
    #~ u'اللا',
    #~ u'الم',
    #~ u'المت',
    #~ u'المتم',
    #~ u'المست',
    #~ u'المن',
    u'ان',
    u'اي',
    u'أ',
    #~ u'أال',
    u'أأ',
    u'أب',
    #~ u'أبال',
    u'أت',
    u'أف',
    #~ u'أفال',
    #~ u'أفب',
    #~ u'أفبال',
    u'أفت',
    #~ u'أل',
    #~ u'ألل',
    u'أو',
    u'أوا',
    #~ u'أوال',
    #~ u'أولل',
    u'أي',
    u'إ',
    u'إست',
    #~ u'ب',
    #~ u'باست',
    #~ u'بال',
    #~ u'بالا',
    #~ u'بالاست',
    #~ u'بالان',
    #~ u'بالأ',
    #~ u'بالإ',
    #~ u'بالت',
    #~ u'بالم',
    #~ u'بالمت',
    #~ u'بالمست',
    #~ u'بان',
    #~ u'بأ',
    #~ u'بإ',
    #~ u'بت',
    #~ u'بم',
    #~ u'بمست',
    u'ت',
    #~ u'تال',
    u'تت',
    u'تست',
    u'تن',
    u'س',
    u'سأ',
    u'ست',
    u'سن',
    u'سنت',
    u'سي',
    u'سيت',
    u'ف',
    u'فا',
    u'فاست',
    #~ u'فال',
    #~ u'فالا',
    #~ u'فالاست',
    #~ u'فالأ',
    #~ u'فالت',
    #~ u'فالم',
    #~ u'فالمست',
    u'فان',
    u'فأ',
    u'فإ',
    #~ u'فب',
    #~ u'فبال',
    #~ u'فبالم',
    u'فت',
    u'فتست',
    u'فس',
    u'فسأ',
    u'فست',
    u'فسن',
    u'فسي',
    u'فك',
    #~ u'فكال',
    u'فل',
    #~ u'فلل',
    #~ u'فللم',
    u'فلي',
    u'فليست',
    #~ u'فم',
    u'فن',
    u'فنت',
    u'فو',
    #~ u'فوال',
    u'في',
    u'فيت',
    u'فيست',
    #~ u'ك',
    #~ u'كاست',
    #~ u'كال',
    #~ u'كالا',
    #~ u'كالاست',
    #~ u'كالان',
    #~ u'كالت',
    #~ u'كالم',
    #~ u'كالمت',
    #~ u'كالمست',
    #~ u'كم',
    #~ u'كمست',
    u'ل',
    u'لا',
    u'لاست',
    #~ u'لال',
    u'لان',
    u'لأ',
    u'لأست',
    u'لإ',
    u'لت',
    #~ u'لل',
    #~ u'للا',
    #~ u'للاست',
    #~ u'للان',
    #~ u'للإ',
    #~ u'للإست',
    #~ u'للت',
    #~ u'للم',
    #~ u'للمت',
    #~ u'للمست',
    #~ u'لم',
    #~ u'لمست',
    u'لي',
    u'ليت',
    u'ليست',
    #~ u'م',
    #~ u'مت',
    #~ u'مست',
    #~ u'من',
    u'ن',
    u'نت',
    u'نست',
    u'و',
    u'وا',
    u'وات',
    u'واست',
    #~ u'وال',
    #~ u'والا',
    #~ u'والاست',
    #~ u'والان',
    #~ u'والأ',
    #~ u'والإ',
    #~ u'والت',
    #~ u'والم',
    #~ u'والمت',
    #~ u'والمست',
    #~ u'والمن',
    u'وان',
    u'وأ',
    u'وأست',
    u'وإ',
    #~ u'وب',
    #~ u'وبال',
    #~ u'وبالأ',
    #~ u'وبالت',
    #~ u'وبالم',
    #~ u'وبالمت',
    #~ u'وبإ',
    #~ u'وبت',
    #~ u'وبم',
    u'وت',
    u'وتت',
    u'وسأ',
    u'وست',
    u'وسن',
    u'وسي',
    #~ u'وك',
    #~ u'وكال',
    u'ول',
    #~ u'ولأ',
    u'ولت',
    u'ولتست',
    #~ u'ولل',
    #~ u'وللا',
    #~ u'وللاست',
    #~ u'وللت',
    #~ u'وللم',
    #~ u'وللمت',
    #~ u'ولم',
    u'ولن',
    u'ولي',
    #~ u'وم',
    #~ u'ومت',
    #~ u'ومست',
    #~ u'ومن',
    u'ون',
    u'وي',
    u'ويت',
    u'ويست',
    u'ي',
    u'يا',
    #~ u'يال',
    #~ u'يالل',
    u'يت',
    u'يست',
    u'ين',
)

VERB_SUFFIX_LIST = (
    u"",
    #~ u'ة',
    u'ا',
    #~ u'اءك',
    #~ u'اءكم',
    #~ u'اءكما',
    #~ u'اءكن',
    #~ u'اءنا',
    #~ u'اءه',
    #~ u'اءها',
    #~ u'اءهم',
    #~ u'اءهما',
    #~ u'اءهن',
    #~ u'اءي',
    #~ u'ائك',
    #~ u'ائكم',
    #~ u'ائكما',
    #~ u'ائكن',
    #~ u'ائنا',
    #~ u'ائه',
    #~ u'ائها',
    #~ u'ائهم',
    #~ u'ائهما',
    #~ u'ائهن',
    #~ u'ائي',
    #~ u'اتك',
    #~ u'اتكم',
    #~ u'اتكما',
    #~ u'اتكن',
    #~ u'اتنا',
    #~ u'اته',
    #~ u'اتها',
    #~ u'اتهم',
    #~ u'اتهما',
    #~ u'اتهن',
    #~ u'اتي',
    #~ u'اتيات',
    #~ u'اتيان',
    #~ u'اتية',
    #~ u'اتيه',
    #~ u'اتيون',
    #~ u'اتيين',
    u'اك',
    u'اكما',
    u'اكن',
    u'ان',
    u'انا',
    #~ u'انات',
    #~ u'اناتك',
    #~ u'اناتكم',
    #~ u'اناتكما',
    #~ u'اناتكن',
    #~ u'اناتنا',
    #~ u'اناته',
    #~ u'اناتها',
    #~ u'اناتهم',
    #~ u'اناتهما',
    #~ u'اناتهن',
    #~ u'اناتي',
    #~ u'انة',
    u'انك',
    u'انكم',
    u'انكما',
    u'انكن',
    u'اننا',
    u'انني',
    u'انه',
    u'انها',
    u'انهم',
    u'انهما',
    u'انهن',
    u'اني',
    #~ u'انيات',
    #~ u'انيان',
    #~ u'انية',
    #~ u'انيتك',
    #~ u'انيتكم',
    #~ u'انيتكما',
    #~ u'انيتكن',
    #~ u'انيتنا',
    #~ u'انيته',
    #~ u'انيتها',
    #~ u'انيتهم',
    #~ u'انيتهما',
    #~ u'انيتهن',
    #~ u'انيتي',
    #~ u'انيون',
    #~ u'انيين',
    u'اها',
    u'اهما',
    u'اهن',
    #~ u'اوات',
    u'اوي',
    #~ u'اوية',
    u'اي',
    u'ت',
    u'تاك',
    u'تاكم',
    u'تاكما',
    u'تاكن',
    u'تان',
    u'تانا',
    u'تاني',
    u'تاه',
    u'تاها',
    u'تاهم',
    u'تاهما',
    u'تاهن',
    u'تاي',
    u'تك',
    u'تكم',
    u'تكما',
    u'تكن',
    u'تم',
    u'تما',
    u'تمانا',
    u'تماني',
    u'تماه',
    u'تماها',
    u'تماهم',
    u'تماهما',
    u'تماهن',
    u'تمونا',
    u'تموني',
    u'تموه',
    u'تموها',
    u'تموهم',
    u'تموهما',
    u'تموهن',
    u'تن',
    u'تنا',
    u'تني',
    u'ته',
    u'تها',
    u'تهم',
    u'تهم',
    u'تهما',
    u'تهن',
    #~ u'تيَّ',
    #~ u'تي',
    #~ u'تيك',
    #~ u'تيكم',
    #~ u'تيكما',
    #~ u'تيكن',
    #~ u'تين',
    #~ u'تينا',
    #~ u'تيه',
    #~ u'تيها',
    #~ u'تيهم',
    #~ u'تيهما',
    #~ u'تيهن',
    u'ك',
    u'ك',
    u'كم',
    u'كم',
    u'كما',
    u'كن',
    u'ن',
    u'نا',
    u'ناك',
    u'ناكم',
    u'ناكما',
    u'ناكن',
    u'ناه',
    u'ناها',
    u'ناهم',
    u'ناهما',
    u'ناهن',
    u'نك',
    u'نكم',
    u'نكما',
    u'نكن',
    u'ننا',
    u'نني',
    u'نه',
    u'نها',
    u'نهم',
    u'نهما',
    u'نهن',
    u'ني',
    u'ه',
    u'ه',
    u'ها',
    u'هم',
    u'هما',
    u'هن',
    u'وا',
    #~ u'وات',
    #~ u'وانية',
    u'وك',
    u'وكم',
    u'وكما',
    u'وكن',
    u'ون',
    u'ونا',
    u'ونك',
    u'ونكم',
    u'ونكما',
    u'ونكن',
    u'وننا',
    u'ونني',
    u'ونه',
    u'ونها',
    u'ونهم',
    u'ونهما',
    u'ونهن',
    u'وني',
    u'وه',
    u'وها',
    u'وهم',
    u'وهما',
    u'وهن',
    u'ي',
    #~ u'يات',
    #~ u'ياتك',
    u'ياتكم',
    #~ u'ياتكما',
    #~ u'ياتكن',
    #~ u'ياتنا',
    #~ u'ياته',
    #~ u'ياتها',
    #~ u'ياتهم',
    #~ u'ياتهن',
    #~ u'ياتهها',
    #~ u'ياتي',
    #~ u'يان',
    #~ u'ية',
    #~ u'يتان',
    #~ u'يتك',
    #~ u'يتكم',
    #~ u'يتكما',
    #~ u'يتكن',
    #~ u'يتنا',
    #~ u'يته',
    #~ u'يتها',
    #~ u'يتهم',
    #~ u'يتهما',
    #~ u'يتهن',
    #~ u'يتي',
    #~ u'يتيا',
    #~ u'يتيان',
    #~ u'يتين',
    u'يك',
    u'يكم',
    u'يكم',
    u'يكما',
    u'يكن',
    u'ين',
    u'ينا',
    u'يننا',
    u'ينني',
    u'ينه',
    u'ينها',
    u'ينهم',
    u'ينهما',
    u'ينهن',
    u'يني',
    u'يه',
    u'يها',
    u'يهم',
    u'يهم',
    u'يهما',
    u'يهن',
    u'يون',
    u'يي',
    u'يين',
)


NOUN_PREFIX_LIST = (
    u"",
    u'ءأ',
    u'ا',
    u'ات',
    u'است',
    u'ال',
    u'الا',
    u'الاست',
    u'الان',
    u'الأ',
    u'الإ',
    u'الت',
    u'اللا',
    u'الم',
    u'المت',
    u'المتم',
    u'المست',
    u'المن',
    u'ان',
    u'اي',
    u'أ',
    u'أال',
    u'أأ',
    u'أب',
    u'أبال',
    u'أت',
    u'أف',
    u'أفال',
    u'أفب',
    u'أفبال',
    u'أفت',
    u'أل',
    u'ألل',
    u'أو',
    u'أوا',
    u'أوال',
    u'أولل',
    u'أي',
    u'إ',
    u'إست',
    u'ب',
    u'باست',
    u'بال',
    u'بالا',
    u'بالاست',
    u'بالان',
    u'بالأ',
    u'بالإ',
    u'بالت',
    u'بالم',
    u'بالمت',
    u'بالمست',
    u'بان',
    u'بأ',
    u'بإ',
    u'بت',
    u'بم',
    u'بمست',
    u'ت',
    u'تال',
    #~ u'تت',
    #~ u'تست',
    #~ u'تن',
    #~ u'س',
    #~ u'سأ',
    #~ u'ست',
    #~ u'سن',
    #~ u'سنت',
    #~ u'سي',
    #~ u'سيت',
    u'ف',
    u'فا',
    u'فاست',
    u'فال',
    u'فالا',
    u'فالاست',
    u'فالأ',
    u'فالت',
    u'فالم',
    u'فالمست',
    u'فان',
    u'فأ',
    u'فإ',
    u'فب',
    u'فبال',
    u'فبالم',
    u'فت',
    #~ u'فتست',
    #~ u'فس',
    #~ u'فسأ',
    #~ u'فست',
    #~ u'فسن',
    #~ u'فسي',
    u'فك',
    u'فكال',
    u'فل',
    u'فلل',
    u'فللم',
    #~ u'فلي',
    #~ u'فليست',
    u'فم',
    #~ u'فن',
    #~ u'فنت',
    u'فو',
    u'فوال',
    #~ u'في',
    #~ u'فيت',
    #~ u'فيست',
    u'ك',
    u'كاست',
    u'كال',
    u'كالا',
    u'كالاست',
    u'كالان',
    u'كالت',
    u'كالم',
    u'كالمت',
    u'كالمست',
    u'كم',
    u'كمست',
    u'ل',
    u'لا',
    u'لاست',
    u'لال',
    u'لان',
    u'لأ',
    u'لأست',
    u'لإ',
    u'لت',
    u'لل',
    u'للا',
    u'للاست',
    u'للان',
    u'للإ',
    u'للإست',
    u'للت',
    u'للم',
    u'للمت',
    u'للمست',
    u'لم',
    u'لمست',
    #~ u'لي',
    #~ u'ليت',
    #~ u'ليست',
    u'م',
    u'مت',
    u'مست',
    u'من',
    #~ u'ن',
    #~ u'نت',
    #~ u'نست',
    u'و',
    u'وا',
    u'وات',
    u'واست',
    u'وال',
    u'والا',
    u'والاست',
    u'والان',
    u'والأ',
    u'والإ',
    u'والت',
    u'والم',
    u'والمت',
    u'والمست',
    u'والمن',
    u'وان',
    u'وأ',
    u'وأست',
    u'وإ',
    u'وب',
    u'وبال',
    u'وبالأ',
    u'وبالت',
    u'وبالم',
    u'وبالمت',
    u'وبإ',
    u'وبت',
    u'وبم',
    u'وت',
    #~ u'وتت',
    #~ u'وسأ',
    #~ u'وست',
    #~ u'وسن',
    #~ u'وسي',
    u'وك',
    u'وكال',
    u'ول',
    u'ولأ',
    u'ولت',
    #~ u'ولتست',
    u'ولل',
    u'وللا',
    u'وللاست',
    u'وللت',
    u'وللم',
    u'وللمت',
    u'ولم',
    #~ u'ولن',
    u'ولي',
    u'وم',
    u'ومت',
    u'ومست',
    u'ومن',
    #~ u'ون',
    #~ u'وي',
    #~ u'ويت',
    #~ u'ويست',
    #~ u'ي',
    u'يا',
    u'يال',
    u'يالل',
    #~ u'يت',
    #~ u'يست',
    #~ u'ين',
)

NOUN_SUFFIX_LIST = (
    u"",
    u'ة',
    u'ا',
    u'اءك',
    u'اءكم',
    u'اءكما',
    u'اءكن',
    u'اءنا',
    u'اءه',
    u'اءها',
    u'اءهم',
    u'اءهما',
    u'اءهن',
    u'اءي',
    u'ائك',
    u'ائكم',
    u'ائكما',
    u'ائكن',
    u'ائنا',
    u'ائه',
    u'ائها',
    u'ائهم',
    u'ائهما',
    u'ائهن',
    u'ائي',
    u'اتك',
    u'اتكم',
    u'اتكما',
    u'اتكن',
    u'اتنا',
    u'اته',
    u'اتها',
    u'اتهم',
    u'اتهما',
    u'اتهن',
    u'اتي',
    u'اتيات',
    u'اتيان',
    u'اتية',
    u'اتيه',
    u'اتيون',
    u'اتيين',
    u'اك',
    u'اكما',
    u'اكن',
    u'ان',
    u'انا',
    u'انات',
    u'اناتك',
    u'اناتكم',
    u'اناتكما',
    u'اناتكن',
    u'اناتنا',
    u'اناته',
    u'اناتها',
    u'اناتهم',
    u'اناتهما',
    u'اناتهن',
    u'اناتي',
    u'انة',
    u'انك',
    u'انكم',
    u'انكما',
    u'انكن',
    u'اننا',
    u'انني',
    u'انه',
    u'انها',
    u'انهم',
    u'انهما',
    u'انهن',
    u'اني',
    u'انيات',
    u'انيان',
    u'انية',
    u'انيتك',
    u'انيتكم',
    u'انيتكما',
    u'انيتكن',
    u'انيتنا',
    u'انيته',
    u'انيتها',
    u'انيتهم',
    u'انيتهما',
    u'انيتهن',
    u'انيتي',
    u'انيون',
    u'انيين',
    u'اها',
    u'اهما',
    u'اهن',
    u'اوات',
    u'اوي',
    u'اوية',
    u'اي',
    u'ت',
    u'تاك',
    u'تاكم',
    u'تاكما',
    u'تاكن',
    u'تان',
    u'تانا',
    u'تاني',
    u'تاه',
    u'تاها',
    u'تاهم',
    u'تاهما',
    u'تاهن',
    u'تاي',
    u'تك',
    u'تكم',
    u'تكما',
    u'تكن',
    u'تم',
    u'تما',
    u'تمانا',
    u'تماني',
    u'تماه',
    u'تماها',
    u'تماهم',
    u'تماهما',
    u'تماهن',
    u'تمونا',
    u'تموني',
    u'تموه',
    u'تموها',
    u'تموهم',
    u'تموهما',
    u'تموهن',
    u'تن',
    u'تنا',
    u'تني',
    u'ته',
    u'تها',
    u'تهم',
    u'تهم',
    u'تهما',
    u'تهن',
    u'تيَّ',
    u'تي',
    u'تيك',
    u'تيكم',
    u'تيكما',
    u'تيكن',
    u'تين',
    u'تينا',
    u'تيه',
    u'تيها',
    u'تيهم',
    u'تيهما',
    u'تيهن',
    u'ك',
    u'ك',
    u'كم',
    u'كم',
    u'كما',
    u'كن',
    #~ u'ن',
    u'نا',
    #~ u'ناك',
    #~ u'ناكم',
    #~ u'ناكما',
    #~ u'ناكن',
    #~ u'ناه',
    #~ u'ناها',
    #~ u'ناهم',
    #~ u'ناهما',
    #~ u'ناهن',
    #~ u'نك',
    #~ u'نكم',
    #~ u'نكما',
    #~ u'نكن',
    #~ u'ننا',
    #~ u'نني',
    #~ u'نه',
    #~ u'نها',
    #~ u'نهم',
    #~ u'نهما',
    #~ u'نهن',
    #~ u'ني',
    u'ه',
    u'ه',
    u'ها',
    u'هم',
    u'هما',
    u'هن',
    u'وا',
    u'وات',
    u'وانية',
    u'وك',
    u'وكم',
    u'وكما',
    u'وكن',
    u'ون',
    u'ونا',
    #~ u'ونك',
    #~ u'ونكم',
    #~ u'ونكما',
    #~ u'ونكن',
    #~ u'وننا',
    #~ u'ونني',
    #~ u'ونه',
    #~ u'ونها',
    #~ u'ونهم',
    #~ u'ونهما',
    #~ u'ونهن',
    #~ u'وني',
    u'وه',
    u'وها',
    u'وهم',
    u'وهما',
    u'وهن',
    u'ي',
    u'يات',
    u'ياتك',
    u'ياتكم',
    u'ياتكما',
    u'ياتكن',
    u'ياتنا',
    u'ياته',
    u'ياتها',
    u'ياتهم',
    u'ياتهن',
    u'ياتهها',
    u'ياتي',
    u'يان',
    u'ية',
    u'يتان',
    u'يتك',
    u'يتكم',
    u'يتكما',
    u'يتكن',
    u'يتنا',
    u'يته',
    u'يتها',
    u'يتهم',
    u'يتهما',
    u'يتهن',
    u'يتي',
    u'يتيا',
    u'يتيان',
    u'يتين',
    u'يك',
    u'يكم',
    u'يكم',
    u'يكما',
    u'يكن',
    u'ين',
    u'ينا',
    u'يننا',
    u'ينني',
    u'ينه',
    u'ينها',
    u'ينهم',
    u'ينهما',
    u'ينهن',
    u'يني',
    u'يه',
    u'يها',
    u'يهم',
    u'يهم',
    u'يهما',
    u'يهن',
    u'يون',
    u'يي',
    u'يين',
)

STEMMING_SUFFIX_LIST = (
    u"",
    u'ة',
    u'ا',
    u'ت',
    u'ات',
    u'ي',
    u'اءك',
    u'اءكم',
    u'اءكما',
    u'اءكن',
    u'اءنا',
    u'اءه',
    u'اءها',
    u'اءهم',
    u'اءهما',
    u'اءهن',
    u'اءي',
    u'ائك',
    u'ائكم',
    u'ائكما',
    u'ائكن',
    u'ائنا',
    u'ائه',
    u'ائها',
    u'ائهم',
    u'ائهما',
    u'ائهن',
    u'ائي',
    u'اتك',
    u'اتكم',
    u'اتكما',
    u'اتكن',
    u'اتنا',
    u'اته',
    u'اتها',
    u'اتهم',
    u'اتهما',
    u'اتهن',
    u'اتي',
    u'اتيات',
    u'اتيان',
    u'اتية',
    u'اتيه',
    u'اتيون',
    u'اتيين',
    u'اك',
    u'اكما',
    u'اكن',
    u'ان',
    u'انا',
    u'انات',
    u'اناتك',
    u'اناتكم',
    u'اناتكما',
    u'اناتكن',
    u'اناتنا',
    u'اناته',
    u'اناتها',
    u'اناتهم',
    u'اناتهما',
    u'اناتهن',
    u'اناتي',
    u'انة',
    u'انك',
    u'انكم',
    u'انكما',
    u'انكن',
    u'اننا',
    u'انني',
    u'انه',
    u'انها',
    u'انهم',
    u'انهما',
    u'انهن',
    u'اني',
    u'انيات',
    u'انيان',
    u'انية',
    u'انيتك',
    u'انيتكم',
    u'انيتكما',
    u'انيتكن',
    u'انيتنا',
    u'انيته',
    u'انيتها',
    u'انيتهم',
    u'انيتهما',
    u'انيتهن',
    u'انيتي',
    u'انيون',
    u'انيين',
    u'اها',
    u'اه',
    u'اهما',
    u'اهن',
    u'اوات',
    u'اوي',
    u'اوية',
    u'اي',
    u'ت',
    u'تاك',
    u'تاكم',
    u'تاكما',
    u'تاكن',
    u'تان',
    u'تانا',
    u'تاني',
    u'تاه',
    u'تاها',
    u'تاهم',
    u'تاهما',
    u'تاهن',
    u'تاي',
    u'تك',
    u'تكم',
    u'تكما',
    u'تكن',
    u'تم',
    u'تما',
    u'تمانا',
    u'تماني',
    u'تماه',
    u'تماها',
    u'تماهم',
    u'تماهما',
    u'تماهن',
    u'تمونا',
    u'تموني',
    u'تموه',
    u'تموها',
    u'تموهم',
    u'تموهما',
    u'تموهن',
    u'تن',
    u'تنا',
    u'تني',
    u'ته',
    u'تها',
    u'تهم',
    u'تهم',
    u'تهما',
    u'تهن',
    u'تيَّ',
    u'تي',
    u'تيك',
    u'تيكم',
    u'تيكما',
    u'تيكن',
    u'تين',
    u'تينا',
    u'تيه',
    u'تيها',
    u'تيهم',
    u'تيهما',
    u'تيهن',
    u'ك',
    u'ك',
    u'كم',
    u'كم',
    u'كما',
    u'كن',
    u'ن',
    u'نا',
    u'ناك',
    u'ناكم',
    u'ناكما',
    u'ناكن',
    u'ناه',
    u'ناها',
    u'ناهم',
    u'ناهما',
    u'ناهن',
    u'نك',
    u'نكم',
    u'نكما',
    u'نكن',
    u'ننا',
    u'نني',
    u'نه',
    u'نها',
    u'نهم',
    u'نهما',
    u'نهن',
    u'ني',
    u'ه',
    u'ه',
    u'ها',
    u'هم',
    u'هما',
    u'هن',
    u'وا',
    u'وات',
    u'وانية',
    u'وك',
    u'وكم',
    u'وكما',
    u'وكن',
    u'ون',
    u'ونا',
    u'ونك',
    u'ونكم',
    u'ونكما',
    u'ونكن',
    u'وننا',
    u'ونني',
    u'ونه',
    u'ونها',
    u'ونهم',
    u'ونهما',
    u'ونهن',
    u'وني',
    u'وه',
    u'وها',
    u'وهم',
    u'وهما',
    u'وهن',
    u'ي',
    u'يات',
    u'ياتك',
    u'ياتكم',
    u'ياتكما',
    u'ياتكن',
    u'ياتنا',
    u'ياته',
    u'ياتها',
    u'ياتهم',
    u'ياتهن',
    u'ياتهها',
    u'ياتي',
    u'يان',
    u'ية',
    u'يتان',
    u'يتك',
    u'يتكم',
    u'يتكما',
    u'يتكن',
    u'يتنا',
    u'يته',
    u'يتها',
    u'يتهم',
    u'يتهما',
    u'يتهن',
    u'يتي',
    u'يتيا',
    u'يتيان',
    u'يتين',
    u'يك',
    u'يكم',
    u'يكم',
    u'يكما',
    u'يكن',
    u'ين',
    u'ينا',
    u'يننا',
    u'ينني',
    u'ينه',
    u'ينها',
    u'ينهم',
    u'ينهما',
    u'ينهن',
    u'يني',
    u'يه',
    u'يها',
    u'يهم',
    u'يهم',
    u'يهما',
    u'يهن',
    u'يون',
    u'يي',
    u'يين',
)


STEMMING_PREFIX_LIST = (
    u"",
    u'ءأ',
    u'ا',
    #~ u'ات',
    #~ u'است',
    #~ u'است',
    u'ال',
    #~ u'الا',
    #~ u'الاست',
    #~ u'الان',
    #~ u'الأ',
    #~ u'الإ',
    #~ u'الت',
    #~ u'اللا',
    #~ u'الم',
    #~ u'المت',
    #~ u'المتم',
    #~ u'المست',
    #~ u'المن',
    #~ u'ان',
    #~ u'اي',
    u'أ',
    #~ u'أال',
    u'أأ',
    u'أب',
    u'أبال',
    u'أت',
    u'أف',
    u'أفال',
    u'أفب',
    u'أفبال',
    u'أفت',
    u'أل',
    u'ألل',
    u'أو',
    u'أوا',
    u'أوال',
    u'أولل',
    u'أي',
    #~ u'إ',
    #~ u'إست',
    u'ب',
    #~ u'باست',
    u'بال',
    #~ u'بالا',
    #~ u'بالاست',
    #~ u'بالان',
    #~ u'بالأ',
    #~ u'بالإ',
    #~ u'بالت',
    #~ u'بالم',
    #~ u'بالمت',
    #~ u'بالمست',
    #~ u'بان',
    #~ u'بأ',
    #~ u'بإ',
    #~ u'بت',
    #~ u'بم',
    #~ u'بمست',
    u'ت',
    #~ u'تال',
    #~ u'تت',
    #~ u'تست',
    #~ u'تن',
    u'س',
    u'سأ',
    u'ست',
    u'سن',
    #~ u'سنت',
    u'سي',
    #~ u'سيت',
    u'ف',
    #~ u'فا',
    #~ u'فاست',
    u'فال',
    #~ u'فالا',
    #~ u'فالاست',
    #~ u'فالأ',
    #~ u'فالت',
    #~ u'فالم',
    #~ u'فالمست',
    #~ u'فان',
    u'فأ',
    u'فإ',
    #~ u'فب',
    #~ u'فبال',
    #~ u'فبالم',
    u'فت',
    #~ u'فتست',
    u'فس',
    u'فسأ',
    u'فست',
    u'فسن',
    u'فسي',
    u'فك',
    #~ u'فكال',
    u'فل',
    #~ u'فلل',
    #~ u'فللم',
    u'فلي',
    #~ u'فليست',
    #~ u'فم',
    u'فن',
    #~ u'فنت',
    u'فو',
    #~ u'فوال',
    u'في',
    #~ u'فيت',
    #~ u'فيست',
    u'ك',
    #~ u'كاست',
    u'كال',
    #~ u'كالا',
    #~ u'كالاست',
    #~ u'كالان',
    #~ u'كالت',
    #~ u'كالم',
    #~ u'كالمت',
    #~ u'كالمست',
    #~ u'كم',
    #~ u'كمست',
    u'ل',
    u'لا',
    #~ u'لاست',
    #~ u'لال',
    #~ u'لان',
    u'لأ',
    #~ u'لأست',
    #~ u'لإ',
    u'لت',
    u'لل',
    #~ u'للا',
    #~ u'للاست',
    #~ u'للان',
    #~ u'للإ',
    #~ u'للإست',
    #~ u'للت',
    #~ u'للم',
    #~ u'للمت',
    #~ u'للمست',
    #~ u'لم',
    #~ u'لمست',
    u'لي',
    #~ u'ليت',
    #~ u'ليست',
    #~ u'م',
    #~ u'مت',
    #~ u'مست',
    #~ u'من',
    u'ن',
    #~ u'نت',
    #~ u'نست',
    u'و',
    u'وا',
    #~ u'وات',
    #~ u'واست',
    u'وال',
    #~ u'والا',
    #~ u'والاست',
    #~ u'والان',
    #~ u'والأ',
    #~ u'والإ',
    #~ u'والت',
    #~ u'والم',
    #~ u'والمت',
    #~ u'والمست',
    #~ u'والمن',
    #~ u'وان',
    u'وأ',
    #~ u'وأست',
    #~ u'وإ',
    u'وب',
    u'وبال',
    #~ u'وبالأ',
    #~ u'وبالت',
    #~ u'وبالم',
    #~ u'وبالمت',
    #~ u'وبإ',
    #~ u'وبت',
    #~ u'وبم',
    u'وت',
    #~ u'وتت',
    u'وسأ',
    u'وست',
    u'وسن',
    u'وسي',
    #~ u'وك',
    #~ u'وكال',
    u'ول',
    #~ u'ولأ',
    u'ولت',
    #~ u'ولتست',
    #~ u'ولل',
    #~ u'وللا',
    #~ u'وللاست',
    #~ u'وللت',
    #~ u'وللم',
    #~ u'وللمت',
    #~ u'ولم',
    u'ولن',
    u'ولي',
    #~ u'وم',
    #~ u'ومت',
    #~ u'ومست',
    #~ u'ومن',
    u'ون',
    u'وي',
    #~ u'ويت',
    #~ u'ويست',
    u'ي',
    u'يا',
    #~ u'يال',
    #~ u'يالل',
    #~ u'يت',
    #~ u'يست',
    #~ u'ين',
)
