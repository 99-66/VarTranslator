import redis
from googletrans import Translator


class VarTranslator:
    """
    한글 단어를 영어 단어로 변경하기 위한 Wrapping Class

    동적으로 수집한 한글 단어를 영어 변수/필드로 사용하기 위한 목적으로 만들었습니다
    메인 라이브러리는 *Reference 를 사용하였습니다

    *Reference: https://github.com/ssut/py-googletrans
    """
    REDIS = {
        'HOST': '',
        'PORT': 6379,
        'PASSWORD': '',
        'DB': 0
    }

    def __init__(self):
        self.translator = Translator()
        self.redis = redis

    @classmethod
    def _connection(cls):
        return redis.StrictRedis(host=cls.REDIS['HOST'], port=cls.REDIS['PORT'],
                                 password=cls.REDIS['PASSWORD'], db=cls.REDIS['DB'],
                                 decode_responses=True)

    def _cache_get(self, kor_word):
        conn = self._connection()
        trans_word = conn.get(kor_word)
        if trans_word:
            return trans_word
        else:
            return False

    def _cache_save(self, kor_word, eng_word):
        conn = self._connection()

        return conn.set(kor_word, eng_word)

    def translate(self, word):
        # Cache 에 이미 등록된 번역 단어가 있다면 바로 리턴
        try:
            trans_word = self._cache_get(word)
        except:
            pass
        else:
            if trans_word:
                return trans_word

        # 단어 번역 및 Cache 에 저장
        try:
            trans_word = self.translator.translate(word)
        except Exception as e:
            raise RuntimeError(f'Translate failed. {repr(e)}')
        else:
            cleaning_word = self._cleaning_word(trans_word.text)
            try:
                self._cache_save(word, cleaning_word)
            except Exception:
                pass

            return cleaning_word

    @staticmethod
    def _cleaning_word(word):
        # 띄어쓰기가 있는 경우 언더바로 변경
        word = word.replace(' ', '_')

        # 위치정보(GPS) 와 같이 되어 있는 경우 '(' 는 '_' 로 변경하고 ')' 는 삭제
        word = word.replace('(', '_').replace(')', '')

        # '/' 문자가 포함되어 있는 경우 삭제
        word = word.replace('/', '')

        # '__' 언더바가 연속으로 있는 경우, 언더바 한개를 삭제
        word = word.replace('__', '_')

        # cleaning 한 단어는 소문자로 리턴
        return word.lower()



