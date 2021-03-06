import os

from boj.__version__ import __version__
from boj.config.settings_directory import SETTINGS_DIRECTORY


DEFAULT_SETTINGS = {
    'version': __version__,

    'doc': '''
        향후 업데이트 시 [DEFAULT] 섹션의 설정은 boj 모듈에 의해 덮어씌워지므로,
        유저 설정은 하단의 [user] 섹션에 입력해주시기 바랍니다.
    ''',

    # config.ini 가 저장되는 경로
    'path.settings.dirname': SETTINGS_DIRECTORY,

    # 임시 소스파일 및 입출력 파일이 보관되는 폴더
    'path.temp.dirname': os.path.join('%(path.settings.dirname)s', 'temp'),

    # 임시 출력 파일명
    'path.temp.stdout.filename': os.path.join('%(path.temp.dirname)s', 'stdout.txt'),

    # 문제 폴더 명 규칙
    'path.problem.dirname': os.path.join('problem', '%(problem.number)s %(problem.title)s'),

    # 읽어올 예제 입출력 파일의 확장명
    'path.inputfile.ext': '.in',
    'path.outputfile.ext': '.out',

    # BOJ로 부터 받아온 예제 입출력 데이터가 저장 될 경로
    'path.data.boj.sample.dirname': os.path.join('%(path.problem.dirname)s', 'data', 'boj', 'sample'),

    # 채점시 시간 제한 (언어별 핸디캡 적용 전)
    'judge.run.timelimit': 4000,

    # 채점 후 소요시간 표시
    'judge.brief.time': True,

    # 각 채점 별 사용 된 입력 데이터 파일명 표시
    'judge.brief.inputfile': True,

    # C++ 언어의 컴파일러 경로
    'language.cpp.compiler.path': 'g++',

    # C 언어의 컴파일러 경로
    'language.c.compiler.path': 'gcc',

    # 파이썬 경로
    'language.python3.python.path': 'python',

    # 깃 경로
    'common.git.path': 'git',

    # 문제 폴더 구성 후 커밋 여부
    'setup.commitAfterSetup': False,

    # 문제 폴더 구성 후 커밋 메시지
    'setup.commitMessage': '%(problem.number)s번 예제 데이터 셋 추가',

    # 문제 폴더 구성 후 더미 파일 생성
    'setup.makeDummyAfterSetup': False,

    # 문제 폴더 구성 후 생성할 더미 파일의 파일명
    'setup.dummyFileName': os.path.join('%(path.problem.dirname)s', '.gitkeep'),
}
