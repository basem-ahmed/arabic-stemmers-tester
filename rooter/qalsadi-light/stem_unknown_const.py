﻿#!/usr/bin/python

# -*- coding=utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        stem_unknown_const
# Purpose:     Arabic lexical analyser constants, provides feature for stemming
#arabic word as unknown
#
# Author:      Taha Zerrouki (taha.zerrouki[at]gmail.com)
#
# Created:     31-10-2011
# Copyright:   (c) Taha Zerrouki 2011
# Licence:     GPL
#-------------------------------------------------------------------------------
"""Arabic lexical analyser constants, provides feature for stemming
arabic word as unknown"""
#from libqutrub.arabic_const import *
import pyarabic.araby as araby
COMP_PREFIX_LETTERS = u"أابتفكلو"
COMP_SUFFIX_LETTERS = u"ينهكماو"
COMP_INFIX_LETTERS = u""
COMP_MAX_PREFIX = 5
COMP_MAX_SUFFIX = 6
COMP_MIN_STEM = 2
COMP_JOKER = u"*"
COMP_PREFIX_LIST_TAGS = {
    "": {
        'tags': (u"", ),
        "vocalized": (u"", )
    },
    u'أ': {
        'tags': (u'استفهام', ),
        "vocalized": (u"أَ", )
    },
    u'و': {
        'tags': (u"", ),
        "vocalized": (u"وَ", )
    },
    u'أو': {
        'tags': (u'استفهام', ),
        "vocalized": (u"أَوََ", )
    },
    u'ف': {
        'tags': (u'عطف', ),
        "vocalized": (u"فَ", )
    },
    u'أف': {
        'tags': (
            u'استفهام',
            u'عطف',
        ),
        "vocalized": (u"أَفَ", )
    },
    u'ب': {
        'tags': (u'جر', ),
        "vocalized": (u"بِ", )
    },
    u'أب': {
        'tags': (
            u'استفهام',
            u'جر',
        ),
        "vocalized": (u"أَبِ", )
    },
    u'وب': {
        'tags': (u'جر', ),
        "vocalized": (u"وَبِ", )
    },
    u'أوب': {
        'tags': (
            u'استفهام',
            u'جر',
        ),
        "vocalized": (u"أَوَبِ", )
    },
    u'فب': {
        'tags': (
            u'عطف',
            u'جر',
        ),
        "vocalized": (u"فَبِ", )
    },
    u'أفب': {
        'tags': (
            u'استفهام',
            u'عطف',
            u'جر',
        ),
        "vocalized": (u"أَفَبِ", )
    },
    u'ك': {
        'tags': (u'جر', ),
        "vocalized": (u"كَ", )
    },
    u'أك': {
        'tags': (
            u'استفهام',
            u'جر',
        ),
        "vocalized": (u"أكَ", )
    },
    u'وك': {
        'tags': (u'جر', ),
        "vocalized": (u"وَكَ", )
    },
    u'أوك': {
        'tags': (
            u'استفهام',
            u'جر',
        ),
        "vocalized": (u"أَوَكَ", )
    },
    u'فك': {
        'tags': (
            u'عطف',
            u'جر',
        ),
        "vocalized": (u"فَكَ", )
    },
    u'أفك': {
        'tags': (
            u'استفهام',
            u'عطف',
            u'جر',
        ),
        "vocalized": (u"أَفَكَ", )
    },
    u'ل': {
        'tags': (u'جر', ),
        "vocalized": (u"لِ", )
    },
    u'أل': {
        'tags': (
            u'استفهام',
            u'جر',
        ),
        "vocalized": (u"أَلِ", )
    },
    u'ول': {
        'tags': (u'جر', ),
        "vocalized": (u"وَلِ", )
    },
    u'أول': {
        'tags': (
            u'استفهام',
            u'جر',
        ),
        "vocalized": (u"أَوَلِ", )
    },
    u'فل': {
        'tags': (
            u'عطف',
            u'جر',
        ),
        "vocalized": (u"فَلِ", )
    },
    u'أفل': {
        'tags': (
            u'استفهام',
            u'عطف',
            u'جر',
        ),
        "vocalized": (u"أَفَلِ", )
    },
    u'ال': {
        'tags': (u'تعريف', ),
        "vocalized": (u"الْ", )
    },
    u'أال': {
        'tags': (
            u'استفهام',
            u'تعريف',
        ),
        "vocalized": (u"أَالْ", )
    },
    u'وال': {
        'tags': (u'تعريف', ),
        "vocalized": (u"وَالْ", )
    },
    u'أوال': {
        'tags': (
            u'استفهام',
            u'تعريف',
        ),
        "vocalized": (u"أَوَالْ", )
    },
    u'فال': {
        'tags': (
            u'عطف',
            u'تعريف',
        ),
        "vocalized": (u"فَالْ", )
    },
    u'أفال': {
        'tags': (
            u'استفهام',
            u'عطف',
            u'تعريف',
        ),
        "vocalized": (u"أَفَالْ", )
    },
    u'بال': {
        'tags': (
            u'جر',
            u'تعريف',
        ),
        "vocalized": (u"بِالْ", )
    },
    u'أبال': {
        'tags': (
            u'استفهام',
            u'جر',
            u'تعريف',
        ),
        "vocalized": (u"أَبالْ", )
    },
    u'وبال': {
        'tags': (
            u'جر',
            u'تعريف',
        ),
        "vocalized": (u"وَبِالْْ", )
    },
    u'أوبال': {
        'tags': (
            u'استفهام',
            u'جر',
            u'تعريف',
        ),
        "vocalized": (u"أَوَبالْْ", )
    },
    u'فبال': {
        'tags': (
            u'عطف',
            u'جر',
            u'تعريف',
        ),
        "vocalized": (u"فَبِالْ", )
    },
    u'أفبال': {
        'tags': (
            u'استفهام',
            u'عطف',
            u'جر',
            u'تعريف',
        ),
        "vocalized": (u"أَفَبِالْ", )
    },
    u'كال': {
        'tags': (
            u'جر',
            u'تعريف',
        ),
        "vocalized": (u"كَالْْ", )
    },
    u'أكال': {
        'tags': (
            u'استفهام',
            u'جر',
            u'تعريف',
        ),
        "vocalized": (u"أكَالْ", )
    },
    u'وكال': {
        'tags': (
            u'جر',
            u'تعريف',
        ),
        "vocalized": (u"وَكَالْْ", )
    },
    u'أوكال': {
        'tags': (
            u'استفهام',
            u'جر',
            u'تعريف',
        ),
        "vocalized": (u"أَوَكَالْْ", )
    },
    u'فكال': {
        'tags': (
            u'عطف',
            u'جر',
            u'تعريف',
        ),
        "vocalized": (u"فَكَالْ", )
    },
    u'أفكال': {
        'tags': (
            u'استفهام',
            u'عطف',
            u'جر',
            u'تعريف',
        ),
        "vocalized": (u"أَفَكَالْ", )
    },
    u'لل': {
        'tags': (
            u'جر',
            u'تعريف',
        ),
        "vocalized": (u"لِلْ", )
    },
    u'ألل': {
        'tags': (
            u'استفهام',
            u'جر',
            u'تعريف',
        ),
        "vocalized": (u"أَلِلْ", )
    },
    u'ولل': {
        'tags': (
            u'جر',
            u'تعريف',
        ),
        "vocalized": (u"وَلِلْ", )
    },
    u'أولل': {
        'tags': (
            u'استفهام',
            u'جر',
            u'تعريف',
        ),
        "vocalized": (u"أَوَلِلْ", )
    },
    u'فلل': {
        'tags': (
            u'عطف',
            u'جر',
            u'تعريف',
        ),
        "vocalized": (u"فَلِلْ", )
    },
    u'أفلل': {
        'tags': (
            u'استفهام',
            u'عطف',
            u'جر',
            u'تعريف',
        ),
        "vocalized": (u"أَفَلِلْ", )
    },
}

COMP_PREFIX_LIST = COMP_PREFIX_LIST_TAGS.keys()
COMP_SUFFIX_LIST_TAGS = {
    "": {
        'tags': (u"", ),
        "vocalized": (u"", )
    },
    u'ي': {
        'tags': (u"مضاف", ),
        "vocalized": (u"ي", ),
    },
    u'ك': {
        'tags': (u"مضاف", ),
        "vocalized": (u"كَ", ),
    },
    u'ه': {
        'tags': (u"مضاف", ),
        "vocalized": (u"هُ", ),
    },
    u'كم': {
        'tags': (u"مضاف", ),
        "vocalized": (u"كُمْ", ),
    },
    u'كن': {
        'tags': (u"مضاف", ),
        "vocalized": (u"كُنَّ", ),
    },
    u'ها': {
        'tags': (u"مضاف", ),
        "vocalized": (u"هَا", ),
    },
    u'هم': {
        'tags': (u"مضاف", ),
        "vocalized": (u"هُمْ", ),
    },
    u'هن': {
        'tags': (u"مضاف", ),
        "vocalized": (u"هُنَّ", ),
    },
    u'نا': {
        'tags': (u"مضاف", ),
        "vocalized": (u"نَا", ),
    },
    u'كما': {
        'tags': (u"مضاف", ),
        "vocalized": (u"كُمَا", ),
    },
    u'هما': {
        'tags': (u"مضاف", ),
        "vocalized": (u"هُمَا", ),
    },
}

COMP_SUFFIX_LIST = COMP_SUFFIX_LIST_TAGS.keys()

COMP_NOUN_AFFIXES = set([
    u'-',  #قصد
    u'أ-',  #أ-قصد
    u'و-',  #و-قصد
    u'أو-',  #أ-و-قصد
    u'ف-',  #ف-قصد
    u'أف-',  #أ-ف-قصد
    u'ب-',  #ب-قصد
    u'أب-',  #أ-ب-قصد
    u'وب-',  #و-ب-قصد
    u'أوب-',  #أ-و-ب-قصد
    u'فب-',  #ف-ب-قصد
    u'أفب-',  #أ-ف-ب-قصد
    u'ك-',  #ك-قصد
    u'أك-',  #أ-ك-قصد
    u'وك-',  #و-ك-قصد
    u'أوك-',  #أ-و-ك-قصد
    u'فك-',  #ف-ك-قصد
    u'أفك-',  #أ-ف-ك-قصد
    u'ل-',  #ل-قصد
    u'أل-',  #أ-ل-قصد
    u'ول-',  #و-ل-قصد
    u'أول-',  #أ-و-ل-قصد
    u'فل-',  #ف-ل-قصد
    u'أفل-',  #أ-ف-ل-قصد
    u'-ي',  #قصد-ي
    u'أ-ي',  #أ-قصد-ي
    u'و-ي',  #و-قصد-ي
    u'أو-ي',  #أ-و-قصد-ي
    u'ف-ي',  #ف-قصد-ي
    u'أف-ي',  #أ-ف-قصد-ي
    u'ب-ي',  #ب-قصد-ي
    u'أب-ي',  #أ-ب-قصد-ي
    u'وب-ي',  #و-ب-قصد-ي
    u'أوب-ي',  #أ-و-ب-قصد-ي
    u'فب-ي',  #ف-ب-قصد-ي
    u'أفب-ي',  #أ-ف-ب-قصد-ي
    u'ك-ي',  #ك-قصد-ي
    u'أك-ي',  #أ-ك-قصد-ي
    u'وك-ي',  #و-ك-قصد-ي
    u'أوك-ي',  #أ-و-ك-قصد-ي
    u'فك-ي',  #ف-ك-قصد-ي
    u'أفك-ي',  #أ-ف-ك-قصد-ي
    u'ل-ي',  #ل-قصد-ي
    u'أل-ي',  #أ-ل-قصد-ي
    u'ول-ي',  #و-ل-قصد-ي
    u'أول-ي',  #أ-و-ل-قصد-ي
    u'فل-ي',  #ف-ل-قصد-ي
    u'أفل-ي',  #أ-ف-ل-قصد-ي
    u'-ك',  #قصد-ك
    u'أ-ك',  #أ-قصد-ك
    u'و-ك',  #و-قصد-ك
    u'أو-ك',  #أ-و-قصد-ك
    u'ف-ك',  #ف-قصد-ك
    u'أف-ك',  #أ-ف-قصد-ك
    u'ب-ك',  #ب-قصد-ك
    u'أب-ك',  #أ-ب-قصد-ك
    u'وب-ك',  #و-ب-قصد-ك
    u'أوب-ك',  #أ-و-ب-قصد-ك
    u'فب-ك',  #ف-ب-قصد-ك
    u'أفب-ك',  #أ-ف-ب-قصد-ك
    u'ك-ك',  #ك-قصد-ك
    u'أك-ك',  #أ-ك-قصد-ك
    u'وك-ك',  #و-ك-قصد-ك
    u'أوك-ك',  #أ-و-ك-قصد-ك
    u'فك-ك',  #ف-ك-قصد-ك
    u'أفك-ك',  #أ-ف-ك-قصد-ك
    u'ل-ك',  #ل-قصد-ك
    u'أل-ك',  #أ-ل-قصد-ك
    u'ول-ك',  #و-ل-قصد-ك
    u'أول-ك',  #أ-و-ل-قصد-ك
    u'فل-ك',  #ف-ل-قصد-ك
    u'أفل-ك',  #أ-ف-ل-قصد-ك
    u'-ه',  #قصد-ه
    u'أ-ه',  #أ-قصد-ه
    u'و-ه',  #و-قصد-ه
    u'أو-ه',  #أ-و-قصد-ه
    u'ف-ه',  #ف-قصد-ه
    u'أف-ه',  #أ-ف-قصد-ه
    u'ب-ه',  #ب-قصد-ه
    u'أب-ه',  #أ-ب-قصد-ه
    u'وب-ه',  #و-ب-قصد-ه
    u'أوب-ه',  #أ-و-ب-قصد-ه
    u'فب-ه',  #ف-ب-قصد-ه
    u'أفب-ه',  #أ-ف-ب-قصد-ه
    u'ك-ه',  #ك-قصد-ه
    u'أك-ه',  #أ-ك-قصد-ه
    u'وك-ه',  #و-ك-قصد-ه
    u'أوك-ه',  #أ-و-ك-قصد-ه
    u'فك-ه',  #ف-ك-قصد-ه
    u'أفك-ه',  #أ-ف-ك-قصد-ه
    u'ل-ه',  #ل-قصد-ه
    u'أل-ه',  #أ-ل-قصد-ه
    u'ول-ه',  #و-ل-قصد-ه
    u'أول-ه',  #أ-و-ل-قصد-ه
    u'فل-ه',  #ف-ل-قصد-ه
    u'أفل-ه',  #أ-ف-ل-قصد-ه
    u'-كم',  #قصد-كم
    u'أ-كم',  #أ-قصد-كم
    u'و-كم',  #و-قصد-كم
    u'أو-كم',  #أ-و-قصد-كم
    u'ف-كم',  #ف-قصد-كم
    u'أف-كم',  #أ-ف-قصد-كم
    u'ب-كم',  #ب-قصد-كم
    u'أب-كم',  #أ-ب-قصد-كم
    u'وب-كم',  #و-ب-قصد-كم
    u'أوب-كم',  #أ-و-ب-قصد-كم
    u'فب-كم',  #ف-ب-قصد-كم
    u'أفب-كم',  #أ-ف-ب-قصد-كم
    u'ك-كم',  #ك-قصد-كم
    u'أك-كم',  #أ-ك-قصد-كم
    u'وك-كم',  #و-ك-قصد-كم
    u'أوك-كم',  #أ-و-ك-قصد-كم
    u'فك-كم',  #ف-ك-قصد-كم
    u'أفك-كم',  #أ-ف-ك-قصد-كم
    u'ل-كم',  #ل-قصد-كم
    u'أل-كم',  #أ-ل-قصد-كم
    u'ول-كم',  #و-ل-قصد-كم
    u'أول-كم',  #أ-و-ل-قصد-كم
    u'فل-كم',  #ف-ل-قصد-كم
    u'أفل-كم',  #أ-ف-ل-قصد-كم
    u'-كن',  #قصد-كن
    u'أ-كن',  #أ-قصد-كن
    u'و-كن',  #و-قصد-كن
    u'أو-كن',  #أ-و-قصد-كن
    u'ف-كن',  #ف-قصد-كن
    u'أف-كن',  #أ-ف-قصد-كن
    u'ب-كن',  #ب-قصد-كن
    u'أب-كن',  #أ-ب-قصد-كن
    u'وب-كن',  #و-ب-قصد-كن
    u'أوب-كن',  #أ-و-ب-قصد-كن
    u'فب-كن',  #ف-ب-قصد-كن
    u'أفب-كن',  #أ-ف-ب-قصد-كن
    u'ك-كن',  #ك-قصد-كن
    u'أك-كن',  #أ-ك-قصد-كن
    u'وك-كن',  #و-ك-قصد-كن
    u'أوك-كن',  #أ-و-ك-قصد-كن
    u'فك-كن',  #ف-ك-قصد-كن
    u'أفك-كن',  #أ-ف-ك-قصد-كن
    u'ل-كن',  #ل-قصد-كن
    u'أل-كن',  #أ-ل-قصد-كن
    u'ول-كن',  #و-ل-قصد-كن
    u'أول-كن',  #أ-و-ل-قصد-كن
    u'فل-كن',  #ف-ل-قصد-كن
    u'أفل-كن',  #أ-ف-ل-قصد-كن
    u'-ها',  #قصد-ها
    u'أ-ها',  #أ-قصد-ها
    u'و-ها',  #و-قصد-ها
    u'أو-ها',  #أ-و-قصد-ها
    u'ف-ها',  #ف-قصد-ها
    u'أف-ها',  #أ-ف-قصد-ها
    u'ب-ها',  #ب-قصد-ها
    u'أب-ها',  #أ-ب-قصد-ها
    u'وب-ها',  #و-ب-قصد-ها
    u'أوب-ها',  #أ-و-ب-قصد-ها
    u'فب-ها',  #ف-ب-قصد-ها
    u'أفب-ها',  #أ-ف-ب-قصد-ها
    u'ك-ها',  #ك-قصد-ها
    u'أك-ها',  #أ-ك-قصد-ها
    u'وك-ها',  #و-ك-قصد-ها
    u'أوك-ها',  #أ-و-ك-قصد-ها
    u'فك-ها',  #ف-ك-قصد-ها
    u'أفك-ها',  #أ-ف-ك-قصد-ها
    u'ل-ها',  #ل-قصد-ها
    u'أل-ها',  #أ-ل-قصد-ها
    u'ول-ها',  #و-ل-قصد-ها
    u'أول-ها',  #أ-و-ل-قصد-ها
    u'فل-ها',  #ف-ل-قصد-ها
    u'أفل-ها',  #أ-ف-ل-قصد-ها
    u'-هم',  #قصد-هم
    u'أ-هم',  #أ-قصد-هم
    u'و-هم',  #و-قصد-هم
    u'أو-هم',  #أ-و-قصد-هم
    u'ف-هم',  #ف-قصد-هم
    u'أف-هم',  #أ-ف-قصد-هم
    u'ب-هم',  #ب-قصد-هم
    u'أب-هم',  #أ-ب-قصد-هم
    u'وب-هم',  #و-ب-قصد-هم
    u'أوب-هم',  #أ-و-ب-قصد-هم
    u'فب-هم',  #ف-ب-قصد-هم
    u'أفب-هم',  #أ-ف-ب-قصد-هم
    u'ك-هم',  #ك-قصد-هم
    u'أك-هم',  #أ-ك-قصد-هم
    u'وك-هم',  #و-ك-قصد-هم
    u'أوك-هم',  #أ-و-ك-قصد-هم
    u'فك-هم',  #ف-ك-قصد-هم
    u'أفك-هم',  #أ-ف-ك-قصد-هم
    u'ل-هم',  #ل-قصد-هم
    u'أل-هم',  #أ-ل-قصد-هم
    u'ول-هم',  #و-ل-قصد-هم
    u'أول-هم',  #أ-و-ل-قصد-هم
    u'فل-هم',  #ف-ل-قصد-هم
    u'أفل-هم',  #أ-ف-ل-قصد-هم
    u'-هن',  #قصد-هن
    u'أ-هن',  #أ-قصد-هن
    u'و-هن',  #و-قصد-هن
    u'أو-هن',  #أ-و-قصد-هن
    u'ف-هن',  #ف-قصد-هن
    u'أف-هن',  #أ-ف-قصد-هن
    u'ب-هن',  #ب-قصد-هن
    u'أب-هن',  #أ-ب-قصد-هن
    u'وب-هن',  #و-ب-قصد-هن
    u'أوب-هن',  #أ-و-ب-قصد-هن
    u'فب-هن',  #ف-ب-قصد-هن
    u'أفب-هن',  #أ-ف-ب-قصد-هن
    u'ك-هن',  #ك-قصد-هن
    u'أك-هن',  #أ-ك-قصد-هن
    u'وك-هن',  #و-ك-قصد-هن
    u'أوك-هن',  #أ-و-ك-قصد-هن
    u'فك-هن',  #ف-ك-قصد-هن
    u'أفك-هن',  #أ-ف-ك-قصد-هن
    u'ل-هن',  #ل-قصد-هن
    u'أل-هن',  #أ-ل-قصد-هن
    u'ول-هن',  #و-ل-قصد-هن
    u'أول-هن',  #أ-و-ل-قصد-هن
    u'فل-هن',  #ف-ل-قصد-هن
    u'أفل-هن',  #أ-ف-ل-قصد-هن
    u'-نا',  #قصد-نا
    u'أ-نا',  #أ-قصد-نا
    u'و-نا',  #و-قصد-نا
    u'أو-نا',  #أ-و-قصد-نا
    u'ف-نا',  #ف-قصد-نا
    u'أف-نا',  #أ-ف-قصد-نا
    u'ب-نا',  #ب-قصد-نا
    u'أب-نا',  #أ-ب-قصد-نا
    u'وب-نا',  #و-ب-قصد-نا
    u'أوب-نا',  #أ-و-ب-قصد-نا
    u'فب-نا',  #ف-ب-قصد-نا
    u'أفب-نا',  #أ-ف-ب-قصد-نا
    u'ك-نا',  #ك-قصد-نا
    u'أك-نا',  #أ-ك-قصد-نا
    u'وك-نا',  #و-ك-قصد-نا
    u'أوك-نا',  #أ-و-ك-قصد-نا
    u'فك-نا',  #ف-ك-قصد-نا
    u'أفك-نا',  #أ-ف-ك-قصد-نا
    u'ل-نا',  #ل-قصد-نا
    u'أل-نا',  #أ-ل-قصد-نا
    u'ول-نا',  #و-ل-قصد-نا
    u'أول-نا',  #أ-و-ل-قصد-نا
    u'فل-نا',  #ف-ل-قصد-نا
    u'أفل-نا',  #أ-ف-ل-قصد-نا
    u'-كما',  #قصد-كما
    u'أ-كما',  #أ-قصد-كما
    u'و-كما',  #و-قصد-كما
    u'أو-كما',  #أ-و-قصد-كما
    u'ف-كما',  #ف-قصد-كما
    u'أف-كما',  #أ-ف-قصد-كما
    u'ب-كما',  #ب-قصد-كما
    u'أب-كما',  #أ-ب-قصد-كما
    u'وب-كما',  #و-ب-قصد-كما
    u'أوب-كما',  #أ-و-ب-قصد-كما
    u'فب-كما',  #ف-ب-قصد-كما
    u'أفب-كما',  #أ-ف-ب-قصد-كما
    u'ك-كما',  #ك-قصد-كما
    u'أك-كما',  #أ-ك-قصد-كما
    u'وك-كما',  #و-ك-قصد-كما
    u'أوك-كما',  #أ-و-ك-قصد-كما
    u'فك-كما',  #ف-ك-قصد-كما
    u'أفك-كما',  #أ-ف-ك-قصد-كما
    u'ل-كما',  #ل-قصد-كما
    u'أل-كما',  #أ-ل-قصد-كما
    u'ول-كما',  #و-ل-قصد-كما
    u'أول-كما',  #أ-و-ل-قصد-كما
    u'فل-كما',  #ف-ل-قصد-كما
    u'أفل-كما',  #أ-ف-ل-قصد-كما
    u'-هما',  #قصد-هما
    u'أ-هما',  #أ-قصد-هما
    u'و-هما',  #و-قصد-هما
    u'أو-هما',  #أ-و-قصد-هما
    u'ف-هما',  #ف-قصد-هما
    u'أف-هما',  #أ-ف-قصد-هما
    u'ب-هما',  #ب-قصد-هما
    u'أب-هما',  #أ-ب-قصد-هما
    u'وب-هما',  #و-ب-قصد-هما
    u'أوب-هما',  #أ-و-ب-قصد-هما
    u'فب-هما',  #ف-ب-قصد-هما
    u'أفب-هما',  #أ-ف-ب-قصد-هما
    u'ك-هما',  #ك-قصد-هما
    u'أك-هما',  #أ-ك-قصد-هما
    u'وك-هما',  #و-ك-قصد-هما
    u'أوك-هما',  #أ-و-ك-قصد-هما
    u'فك-هما',  #ف-ك-قصد-هما
    u'أفك-هما',  #أ-ف-ك-قصد-هما
    u'ل-هما',  #ل-قصد-هما
    u'أل-هما',  #أ-ل-قصد-هما
    u'ول-هما',  #و-ل-قصد-هما
    u'أول-هما',  #أ-و-ل-قصد-هما
    u'فل-هما',  #ف-ل-قصد-هما
    u'أفل-هما',  #أ-ف-ل-قصد-هما
    u'ال-',  #ال-قصد
    u'أال-',  #أ-ال-قصد
    u'وال-',  #و-ال-قصد
    u'أوال-',  #أ-و-ال-قصد
    u'فال-',  #ف-ال-قصد
    u'أفال-',  #أ-ف-ال-قصد
    u'بال-',  #ب-ال-قصد
    u'أبال-',  #أ-ب-ال-قصد
    u'وبال-',  #و-ب-ال-قصد
    u'أوبال-',  #أ-و-ب-ال-قصد
    u'فبال-',  #ف-ب-ال-قصد
    u'أفبال-',  #أ-ف-ب-ال-قصد
    u'كال-',  #ك-ال-قصد
    u'أكال-',  #أ-ك-ال-قصد
    u'وكال-',  #و-ك-ال-قصد
    u'أوكال-',  #أ-و-ك-ال-قصد
    u'فكال-',  #ف-ك-ال-قصد
    u'أفكال-',  #أ-ف-ك-ال-قصد
    u'لل-',  #ل-ال-قصد
    u'ألل-',  #أ-ل-ال-قصد
    u'ولل-',  #و-ل-ال-قصد
    u'أولل-',  #أ-و-ل-ال-قصد
    u'فلل-',  #ف-ل-ال-قصد
    u'أفلل-',  #أ-ف-ل-ال-قصد
])
CONJ_PREFIX_LETTERS = u"1"
CONJ_SUFFIX_LETTERS = u"اتةنوي"
CONJ_INFIX_LETTERS = u""
CONJ_MAX_PREFIX = 3
CONJ_MAX_SUFFIX = 3
CONJ_MIN_STEM = 2
CONJ_JOKER = u"*"
CONJ_PREFIX_LIST = ("")

CONJ_SUFFIX_LIST_TAGS = {
    u"": {
        'tags': (u'', u'مجرور'),
        'vocalized': (araby.DAMMA, araby.KASRA, araby.FATHA, araby.DAMMATAN,
                      araby.KASRATAN)
    },
    u"ُ": {
        'tags': (u'مرفوع', ),
        'vocalized': (u"ُ", )
    },  #TEH_MARBUTA,
    u"ٌ": {
        'tags': (u'مرفوع', u"تنوين"),
        'vocalized': (u"ٌ", )
    },  #TEH_MARBUTA,
    u'ٍ': {
        'tags': (u'مجرور', u"تنوين"),
        'vocalized': (u'ٍ', )
    },  #TEH_MARBUTA,
    u'ِ': {
        'tags': (u'مجرور', ),
        'vocalized': (u'ِ', )
    },  #TEH_MARBUTA,
    u'َ': {
        'tags': (u'منصوب', ),
        'vocalized': (u'َ', )
    },  #TEH_MARBUTA,
    #u"ً":{'tags':(u'منصوب', u"تنوين"), 'vocalized':(u"ً",)},#TEH_MARBUTA,
    u"ة": {
        'tags': (u'مؤنث', u'مجرور'),
        'vocalized': (u"َةُ", u"َةٌ", u'َةٍ', u'َةِ', u'َةَ', u"َةً")
    },  #TEH_MARBUTA,
    u"َةُ": {
        'tags': (u'مؤنث', u'مرفوع'),
        'vocalized': (u"َةُ", )
    },  #TEH_MARBUTA,
    u"َةٌ": {
        'tags': (u'مؤنث', u'مرفوع', u"تنوين"),
        'vocalized': (u"َةٌ", )
    },  #TEH_MARBUTA,
    u'َةٍ': {
        'tags': (u'مؤنث', u'مجرور', u"تنوين"),
        'vocalized': (u'َةٍ', )
    },  #TEH_MARBUTA,
    u'َةِ': {
        'tags': (u'مؤنث', u'مجرور'),
        'vocalized': (u'َةِ', )
    },  #TEH_MARBUTA,
    u'َةَ': {
        'tags': (u'مؤنث', u'منصوب'),
        'vocalized': (u'َةَ', )
    },  #TEH_MARBUTA,
    u"َةً": {
        'tags': (u'مؤنث', u'منصوب', u"تنوين"),
        'vocalized': (u"َةً", )
    },  #TEH_MARBUTA,
    u"ية": {
        'tags': (u'مؤنث', u'مجرور', u'منسوب'),
        'vocalized': (u"ِيَّةُ", u"ِيَّةٌ", u'ِيَّةٍ', u'ِيَّةِ', u'ِيَّةَ',
                      u"ِيَّةً")
    },  #TEH_MARBUTA,
    u"ِيَّةُ": {
        'tags': (u'مؤنث', u'مرفوع', u'منسوب'),
        'vocalized': (u"ِيَّةُ", )
    },  #TEH_MARBUTA,
    u"ِيَّةٌ": {
        'tags': (u'مؤنث', u'مرفوع', u"تنوين", u'منسوب'),
        'vocalized': (u"ِيَّةٌ", )
    },  #TEH_MARBUTA,
    u'ِيَّةٍ': {
        'tags': (u'مؤنث', u'مجرور', u"تنوين", u'منسوب'),
        'vocalized': (u'ِيَّةٍ', )
    },  #TEH_MARBUTA,
    u'ِيَّةِ': {
        'tags': (u'مؤنث', u'مجرور', u'منسوب'),
        'vocalized': (u'ِيَّةِ', )
    },  #TEH_MARBUTA,
    u'ِيَّةَ': {
        'tags': (u'مؤنث', u'منصوب', u'منسوب'),
        'vocalized': (u'ِيَّةَ', )
    },  #TEH_MARBUTA,
    u"ِيَّةً": {
        'tags': (u'مؤنث', u'منصوب', u"تنوين", u'منسوب'),
        'vocalized': (u"ِيَّةً", )
    },  #TEH_MARBUTA,
    u"ا": {
        'tags': (
            u'مثنى',
            u'مضاف',
        ),
        'vocalized': (u'َا', u'ًا')
    },  #ALEF,
    u"َا": {
        'tags': (
            u'مثنى',
            u'مضاف',
        ),
        'vocalized': (u'َا', )
    },  #ALEF,
    u"ًا": {
        'tags': (u'تنوين', ),
        'vocalized': (u'ًا', )
    },  #ALEF,

    #u"ت":{'tags':(u'مؤنث',u'مضاف',u'مجرور'),'vocalized':(u'َت',)},#TEH_MARBUTA,
    #u"يت":{'tags':(u'مضاف',u'مجرور'),'vocalized':(u'َيَّتَ',)},#YEH+TEH_MARBUTA,
    u"ات": {
        'tags': (u'جمع مؤنث سالم', u'مجرور', u'جمع'),
        'vocalized': (u'َاتُ', u'َاتٌ', u'َاتٍ', u'َاتِ')
    },  #ALEF+TEH,
    u'َاتُ': {
        'tags': (u'جمع مؤنث سالم', u'مرفوع', u'جمع'),
        'vocalized': (u'َاتُ', )
    },  #ALEF+TEH,
    u'َاتٌ': {
        'tags': (u'جمع مؤنث سالم', u'مرفوع', u'تنوين', u'جمع'),
        'vocalized': (u'َاتٌ', )
    },  #ALEF+TEH,
    u'َاتٍ': {
        'tags': (u'جمع مؤنث سالم', u'مجرور', u'منصوب', u'تنوين', u'جمع'),
        'vocalized': (u'َاتٍ', )
    },  #ALEF+TEH,
    u'َاتِ': {
        'tags': (u'جمع مؤنث سالم', u'مجرور', u'منصوب', u'جمع'),
        'vocalized': (u'َاتِ', )
    },  #ALEF+TEH,
    u"ون": {
        'tags': (u'جمع مذكر سالم', u'لايضاف', u'جمع'),
        'vocalized': (u'ُونَ', )
    },  #WAW+NOON,
    u'ُونَ': {
        'tags': (u'جمع مذكر سالم', u'لايضاف', u'جمع'),
        'vocalized': (u'ُونَ', )
    },  #WAW+NOON,
    u"ين": {
        'tags': (u'جمع مذكر سالم', u'مجرور', u'لايضاف', u'جمع'),
        'vocalized': (u'ِينَ', u'َيْنِ')
    },  #YEH+NOON,
    u'ِينَ': {
        'tags': (u'جمع مذكر سالم', u'مجرور', u'لايضاف', u'جمع'),
        'vocalized': (u'ِينَ', )
    },  #YEH+NOON,
    u'َيْنِ': {
        'tags': (u'جمع مذكر سالم', u'منصوب', u'لايضاف', u'جمع'),
        'vocalized': (u'َيْنِ', )
    },  #YEH+NOON,
    u"و": {
        'tags': (u'جمع مذكر سالم', u'مضاف', u'جمع'),
        'vocalized': (u'ُو', )
    },  #WAW,
    u'ُو': {
        'tags': (u'جمع مذكر سالم', u'مضاف', u'جمع'),
        'vocalized': (u'ُو', )
    },  #WAW,
    u"ي": {
        'tags': (u'جمع مذكر سالم', u'مضاف', u'مجرور', u'جمع'),
        'vocalized': (u'ِيِ', )
    },  #YEH,
    u'ِيِ': {
        'tags': (u'جمع مذكر سالم', u'مضاف', u'مجرور', u'جمع'),
        'vocalized': (u'ِيِ', u'َيْ')
    },  #YEH,
    u'َيِْ': {
        'tags': (u'جمع مذكر سالم', u'مضاف', u'منصوب', u'جمع'),
        'vocalized': (u'ِيِ', )
    },  #YEH,
    u"ان": {
        'tags': (u'مثنى', u'لايضاف'),
        'vocalized': (u'َانِ', )
    },  #ALEF+NOON,
    u'َانِ': {
        'tags': (u'مثنى', u'لايضاف'),
        'vocalized': (u'َانِ', )
    },  #ALEF+NOON,
    u"تين": {
        'tags': (u'مثنى', u'مجرور', u'لايضاف'),
        'vocalized': (u'َتَيْنِ', )
    },  #TEH+YEH+NOON,
    u'َتَيْنِ': {
        'tags': (u'مثنى', u'مجرور', u'لايضاف'),
        'vocalized': (u'َتَيْنِ', )
    },  #TEH+YEH+NOON,
    u"تان": {
        'tags': (u'مثنى', u'لايضاف'),
        'vocalized': (u'َتَانِِ', )
    },  #TEH+ALEF+NOON,
    u'َتَانِِ': {
        'tags': (u'مثنى', u'لايضاف'),
        'vocalized': (u'َتَانِِ', )
    },  #TEH+ALEF+NOON,
    u"يتين": {
        'tags': (u'مثنى', u'مجرور', u'لايضاف'),
        'vocalized': (u'ِيَّتَيْنِ', )
    },  #TEH+YEH+NOON,
    u'ِيَّتَيْنِ': {
        'tags': (u'مثنى', u'مجرور', u'لايضاف'),
        'vocalized': (u'ِيَّتَيْنِ', )
    },  #TEH+YEH+NOON,
    u"يتان": {
        'tags': (u'مثنى', u'لايضاف'),
        'vocalized': (u'ِيَّتَانِِ', )
    },  #TEH+ALEF+NOON,
    u'ِيَّتَانِِ': {
        'tags': (u'مثنى', u'لايضاف'),
        'vocalized': (u'ِيَّتَانِِ', )
    },  #TEH+ALEF+NOON,
    u"يات": {
        'tags': (u'جمع مؤنث سالم', u'مجرور', u'جمع'),
        'vocalized': (
            u'ِيَاتِ',
            u'ِيَاتُ',
            u'ِيَاتٌ',
            u'ِيَاتٍ',
        )
    },  #YEH+ALEF+TEH,
    u'ِيَاتُ': {
        'tags': (u'جمع مؤنث سالم', u'مرفوع', u'جمع'),
        'vocalized': (u'ِيَاتُ', )
    },  #YEH+ALEF+TEH,
    u'ِيَاتٌ': {
        'tags': (u'جمع مؤنث سالم', u'مرفوع', u'تنوين', u'جمع'),
        'vocalized': (u'ِيَاتٌ', )
    },  #YEH+ALEF+TEH,
    u'ِيَاتِ': {
        'tags': (u'جمع مؤنث سالم', u'مجرور', u'منصوب', u'جمع'),
        'vocalized': (u'ِيَاتِ', )
    },  #YEH+ALEF+TEH,
    u'ِيَاتٍ': {
        'tags': (u'جمع مؤنث سالم', u'مجرور', u'منصوب', u'تنوين', u'جمع'),
        'vocalized': (u'ِيَاتٍ', )
    },  #YEH+ALEF+TEH,
}
CONJ_SUFFIX_LIST = CONJ_SUFFIX_LIST_TAGS.keys()

NOMINAL_CONJUGATION_AFFIX = set([
    u"-",
    u"-ة",  #TEH_MARBUTA,
    u"-ية",  #YEH+TEH_MARBUTA,
    u"-يتين",  #TEH_MARBUTA,
    u"-يتان",  #YEH+TEH_MARBUTA,
    u"-ا",  #ALEF,
    u"-ات",  #ALEF+TEH,
    u"-ون",  #WAW+NOON,
    u"-ين",  #YEH+NOON,
    u"-و",  #WAW,
    u"-ي",  #YEH,
    u"-ان",  #ALEF+NOON,
    u"-تين",  #TEH+YEH+NOON,
    u"-تان",  #TEH+ALEF+NOON,
    u"-يات",  #YEH+ALEF+TEH,
])
