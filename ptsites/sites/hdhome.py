from ..schema.nexusphp import AttendanceHR


class MainClass(AttendanceHR):
    URL = 'https://hdhome.org/'
    USER_CLASSES = {
        'downloaded': [8796093022208],
        'share_ratio': [5.5],
        'days': [70]
    }
