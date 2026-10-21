# 多多중국어 · 다다의 중국 이야기

[다다의 네이버 블로그](https://blog.naver.com/dadablog888) 글을 소개하는 **이미지 없는 정적 HTML 사이트**입니다. 제목, 원문 게시일, 독립적인 소개와 요약, 관련 주제, 네이버 원문 링크를 제공합니다. 검색엔진과 방문자에게 동일한 HTML을 제공하며 JavaScript 실행이나 자동 리다이렉션에 의존하지 않습니다.

배포 대상: **https://dadablog888.github.io/blog/**

2026-10-21 공개 주소는 HTTP 404였습니다. 로그인된 Pages 설정은 기본 도메인 `dadablog888.github.io`, 사용자 지정 도메인 없음, `Deploy from a branch`로 확인했습니다. `main` 빌드 안내와 `None` 선택값이 함께 보여 실제 배포 소스는 최종 확인이 필요합니다. 이번 작업에서 설정 저장·커밋·push·배포는 실행하지 않았습니다.

## 계속 쌓이는 글의 구조

| URL | 역할 |
| --- | --- |
| `/blog/` | 최근 10개의 글, 주제별 탐색, 전체 기록으로 연결 |
| `/blog/posts/<고정-slug>/` | 각 글의 영구 소개 페이지. 제목이 바뀌어도 slug는 유지 |
| `/blog/archive/` | 모든 연도 목록 |
| `/blog/archive/2026/` | 해당 연도의 월 목록 |
| `/blog/archive/2026/10/` | 해당 월의 글 제목·요약 목록 |
| `/blog/archive/2026/10/page/2/` | 31개 이상일 때 생성되는 다음 목록 페이지 |
| `/blog/topics/<주제>/` | 날짜와 별개로 주제별 글 탐색. 30개를 초과하면 `/page/2/` 등 생성 |

글이 있는 연도와 월만 생성합니다. 별도의 일별 아카이브는 만들지 않으며 하루의 글은 개별 소개 페이지로 제공됩니다. 목록은 게시일 내림차순, 페이지당 최대 30개입니다. 메인의 최신 목록에서 빠져도 저장된 글은 유지되고 월별·주제별 목록에서 접근할 수 있습니다. 페이지마다 고유한 canonical과 실제 HTML 링크가 있습니다.

초기 데이터는 2026-10-21에 확인한 최근 10개입니다. **과거 블로그 글 전체를 가져오거나 자동 수집·예약 실행을 설정한 것은 아닙니다.** 새 글을 추가할 때 기존 데이터를 덮어쓰지 않고 누적해야 합니다.

## 실행과 수정

Python 3.9 이상만 필요합니다. npm 설치나 외부 폰트, 이미지 서버가 필요하지 않습니다.

```sh
python3 scripts/build.py
python3 scripts/serve.py
```

브라우저에서 **http://127.0.0.1:8000/blog/** 를 엽니다. 실제 배포와 동일한 `/blog/` 경로를 사용합니다. 파일을 직접 열면 CSS와 내부 링크의 절대 경로가 동작하지 않으므로 HTTP 서버로 확인하세요. 포트 변경: `python3 scripts/serve.py --port 8001`.

`content/posts.json`에 새 항목을 추가합니다. 기존 항목을 최신 10개로 교체하거나 기존 slug를 변경하지 마세요. 새 글의 slug는 원문 게시물 ID처럼 변하지 않는 값을 권장합니다. 최초 작성한 10개의 설명형 slug도 그대로 유지합니다.

- `id`: 네이버 게시물 ID. 중복 금지.
- `slug`: 소개 페이지의 고정 경로.
- `originalTitle`, `publishedAt`, `sourceUrl`: 실제 원문에서 확인한 정보. 게시일은 KST 시각 포함.
- `title`, `description`, `summary`, `sections`, `takeaways`: 직접 확인한 본문을 바탕으로 새로 쓴 소개.
- `keywords`: 실제 내용에 맞는 관련 검색 표현. 검색량 지표를 확인했다는 뜻은 아닙니다.
- `topic`: `content/site.json`에 정의한 주제의 slug.
- `introUpdatedOn`: 해당 소개를 실제 작성·확인·수정한 날짜. 원문 게시일과 구별.
- `related`: 실제로 존재하는 관련 글의 ID 목록.
- `noindex`: 본문 정보가 부족해 검색에서 제외할 때만 `true`.

수정 후 `python3 scripts/build.py`로 HTML·사이트맵·분석 문서를 생성합니다. 생성된 HTML도 함께 저장소에 포함합니다. GitHub Pages에서는 Python을 실행하지 않고 파일을 그대로 제공합니다. HTML을 직접 수정하면 다음 생성 때 덮어써집니다. 글을 삭제하거나 경로를 변경할 때는 이전 생성 폴더도 별도로 정리하고 공개 URL의 이동 처리를 검토하세요.

`content/site.json`에서 배포 주소와 블로그 정보, 분류, 확인일을 관리합니다. 주소를 바꾸면 `url`을 HTTPS와 마지막 `/`를 포함한 실제 주소로 수정한 뒤 다시 생성하세요. canonical·OG·내부 링크·sitemap·robots의 Sitemap 주소가 함께 바뀝니다. `googleSiteVerification`에는 Search Console에서 받은 실제 인증 토큰을 넣을 수 있습니다.

사이트맵의 글별 `lastmod`는 `introUpdatedOn`을 사용합니다. 새 글 추가만으로 예전 글의 수정일을 바꾸지 않습니다. 해당 월·연도·주제 목록은 포함된 소개의 최신 수정일을 사용합니다.

## 파일 구성

| 파일 | 역할 |
| --- | --- |
| `index.html`, `posts/`, `topics/`, `archive/` | 배포할 정적 문서 |
| `assets/style.css` | 읽기 중심의 작은 반응형 스타일. 사진·장식 이미지 없음 |
| `content/posts.json`, `content/site.json` | 누적 콘텐츠와 사이트 설정 |
| `scripts/build.py` | 정적 문서·날짜별 목록·페이지 나누기·사이트맵 생성 |
| `scripts/serve.py` | 실제 프로젝트 경로를 재현하는 미리보기 |
| `scripts/check.py` | 문서·링크·메타데이터·확장 동작 확인 |
| `sitemap.xml`, `robots.txt`, `.nojekyll` | 검색 안내와 정적 Pages 제공 |
| `docs/content-analysis.md` | 확인한 10개 게시물의 제목·게시일·원문 URL·핵심 내용·키워드 |
| `docs/seo-and-publishing.md` | Pages 배포·Search Console 등록 안내 |
| `docs/verification.md` | 최종 검증 결과 |
| `plan/implementation.md` | 작업 계획과 추가 요구 반영 |

## 검증

미리보기 서버를 실행해 둔 상태에서:

```sh
python3 scripts/check.py --http http://127.0.0.1:8000 --sources --growth
git diff --check
```

`--sources`는 네이버 짧은 원문 URL과 실제 본문 페이지를 읽어 제목과 본문 존재 여부를 확인합니다. `--growth`는 저장소 밖 임시 디렉터리에서 가상 글 70개를 추가해 최신 10개 제한, 과거 글 보존, 연도 변경, 월별·주제별 페이지 나누기를 검증합니다. 가상 글은 실제 사이트에 추가하지 않습니다.

## SEO 적용과 한계

- 19개 문서의 고유 제목·설명·self canonical·OG 메타데이터.
- WebSite, CollectionPage, ItemList, WebPage, BreadcrumbList와 원문의 BlogPosting 출처 정보.
- 원문 게시일과 소개 확인·수정일 분리. 사용자에게 보이는 정보와 구조화 데이터 일치.
- 일반 HTML 링크로 최근 글·주제·연도·월·관련 글·네이버 원문 연결.
- 사진과 OG 이미지는 사용하지 않음. 이미지 검색 최적화는 이 사이트의 범위에 포함하지 않음.
- 빈 제목·짧은 본문 글과 그 글만 있는 일상 분류는 `noindex, follow`. 방문자는 읽을 수 있으며 사이트맵에서 제외. 현재 17개 URL이 사이트맵에 포함됨.
- 호스트 루트의 robots.txt만 크롤링 규칙으로 적용됨. `/blog/robots.txt`만으로 설정이 끝나지 않으므로 Search Console에 사이트맵을 직접 제출.

자세한 절차는 [배포와 검색 등록](docs/seo-and-publishing.md)을 확인하세요. 검색 노출이나 순위는 보장되지 않습니다.

제안 커밋 메시지: `feat: add text-first China journal with permanent posts and date archives`
