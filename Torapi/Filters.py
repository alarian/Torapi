# -*- coding: utf-8 -*-
class Category(object):
	XXX = "4"
	MOVIES_XVID = "14"
	MOVIES_X264 = "17"
	TV_EPISODES = "18"
	MUSIC_MP3 = "23"
	MUSIC_FLAC = "25"
	GAMES_PC_ISO = "27"
	GAMES_PC_RIP = "28"
	GAMES_XBOX360 = "32"
	SOFTWARE_PC_ISO = "33"
	EBOOKS = "35"
	GAMES_PS3 = "40"
	TV_HD_EPISODES = "41"
	MOVIES_FULL_BD = "42"
	MOVIES_X264_1080 = "44"
	MOVIES_X264_720 = "45"
	MOVIES_BD_REMUX = "46"
	MOVIES_X264_3D = "47"
	MOVIES_XVID_720 = "48"
	MOVIES = "movies"
	TV = "tv"
	TV_SHOWS = "1;18;41"
	GAMES = "1;27;28;29;30;31;32;40"
	MUSIC = "1;23;24;25;26"
	SOFTWARE = "1;33;34;43"
	NON_XXX = "1;14;15;16;17;21;22;42;18;19;41;27;28;29;30;31;32;40;23;24;25;26;33;34;43;44;45;46;47;48"
	ALL = "1;4;14;15;16;17;21;22;42;18;19;41;27;28;29;30;31;32;40;23;24;25;26;33;34;43;44;45;46;47;48"

class Sort(object):
	SEEDERS = "seeders"
	LEECHERS = "leechers"
	LAST = "last"