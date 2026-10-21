# 배포와 Google 검색 등록

## 배포 상태 및 기준 URL

기준 주소는 `https://dadablog888.github.io/blog/`입니다. 원격 저장소 `https://github.com/dadablog888/blog`와 기존 README, 로그인된 Pages 설정의 기본 도메인에서 확인한 경로입니다. 2026-10-21 공개 주소는 HTTP 404였으며, 운영 중인 사이트의 배포 성공까지 확인된 상태는 아닙니다. 이번 작업은 로컬 구현까지만 수행했습니다.

로그인된 설정에서는 `Deploy from a branch`와 `main` 빌드 안내, `None` 선택값이 함께 보였습니다. 설정을 저장하지 않았으므로 실제 게시 소스는 사용자가 최종 확인해야 합니다.

코드를 검토하고 사용자가 별도로 커밋·push한 뒤, [저장소 Pages 설정](https://github.com/dadablog888/blog/settings/pages)에서 다음을 확인하세요.

1. **Source**: `Deploy from a branch`.
2. **Branch**: `main`, 폴더: `/ (root)`.
3. 필요할 때 설정을 저장한 후 **Actions**의 `pages build and deployment`가 성공했는지 확인.
4. 메인, 글별 소개, CSS, 날짜별 목록, `/blog/sitemap.xml`이 HTTPS에서 200을 반환하는지 확인.
5. 다른 주소나 사용자 지정 도메인을 사용할 경우 `content/site.json`의 `url`을 바꾸고 `python3 scripts/build.py`로 다시 생성.

`.nojekyll`과 생성된 HTML이 있으므로 Pages에서 npm이나 Python 빌드를 설정할 필요가 없습니다. [GitHub Pages 게시 소스 공식 안내](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)를 참고하세요.

## Search Console 소유권 확인

1. [Google Search Console](https://search.google.com/search-console)에 로그인합니다.
2. **URL 접두어** 속성으로 `https://dadablog888.github.io/blog/`를 추가합니다. `github.io` 전체 도메인의 DNS를 소유한 것은 아니므로 그 도메인의 DNS 인증을 시도할 필요가 없습니다.
3. **HTML 태그** 인증을 선택합니다. 제공된 태그의 `content` 토큰 값만 `content/site.json`의 `googleSiteVerification`에 넣습니다.
4. `python3 scripts/build.py`로 다시 생성하고 해당 변경을 사용자가 배포합니다. 토큰은 Google이 제공한 실제 값만 사용합니다.
5. 공개 홈페이지 소스의 `<head>`에 인증 태그가 나타나면 Search Console에서 **확인**합니다. 확인 이후에도 태그를 유지합니다.

[속성 추가 공식 안내](https://support.google.com/webmasters/answer/34592?hl=ko), [소유권 확인 공식 안내](https://support.google.com/webmasters/answer/9008080?hl=ko).

## 사이트맵 제출과 색인 점검

- **Sitemaps**에서 `https://dadablog888.github.io/blog/sitemap.xml`을 제출합니다. URL 접두어가 입력창에 미리 표시되어 있으면 `sitemap.xml`만 입력합니다.
- 사이트맵에는 홈 1개, 주제 4개, 글 소개 9개, 전체·연도·월 목록 3개로 총 17개 URL이 있습니다. 의도적으로 `noindex`한 제목 없는 글과 일상 분류는 제외했습니다.
- **URL 검사**에서 메인과 대표 글 소개를 검사하고, **실제 URL 테스트**로 크롤링 가능 여부를 확인한 뒤 필요한 페이지에 색인 생성을 요청합니다.
- **페이지 색인 생성** 보고서에서 차단, 찾을 수 없음, 중복, Google이 선택한 canonical을 확인합니다. 노출 이후에는 **실적**에서 검색어·클릭·노출·클릭률을 확인합니다.
- 구조화 데이터는 [Schema Markup Validator](https://validator.schema.org/)로 문법과 어휘를 점검할 수 있습니다. [Google 리치 결과 테스트](https://search.google.com/test/rich-results)도 참고하되, WebPage·ItemList 같은 스키마가 리치 결과 유형으로 표시되지 않을 수 있으며 오류를 뜻하지는 않습니다.

사이트맵과 색인 요청은 발견을 돕는 수단이며, 색인·노출·순위를 보장하지 않습니다. [사이트맵 공식 안내](https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview), [URL 검사 공식 안내](https://support.google.com/webmasters/answer/9012289?hl=ko).

## robots.txt의 프로젝트 경로 한계

검색엔진이 적용하는 파일은 **`https://dadablog888.github.io/robots.txt`**입니다. 이 저장소의 파일은 배포 시 `https://dadablog888.github.io/blog/robots.txt`에 놓이므로, 호스트 전체의 크롤링 규칙으로 적용되지 않습니다. `/blog/robots.txt`만으로 검색엔진 설정이 끝났다고 해석하면 안 됩니다.

이 사이트는 각 HTML에 index/noindex 메타태그를 명시하고, 사이트맵은 Search Console로 직접 제출합니다. 루트 robots 파일을 관리하려면 별도의 `dadablog888.github.io` 사용자 사이트 저장소에서 호스트 루트에 파일을 제공해야 합니다. 기존 루트 규칙이 있다면 다른 프로젝트에 미치는 영향을 확인한 후 아래 Sitemap 행을 추가하세요.

```text
User-agent: *
Allow: /

Sitemap: https://dadablog888.github.io/blog/sitemap.xml
```

현재 저장소만 수정해서 호스트 루트 파일을 배포할 수는 없습니다. 별도 사용자 사이트를 이번 작업에서 생성하지 않았습니다. [robots.txt 위치와 범위 공식 설명](https://developers.google.com/search/docs/crawling-indexing/robots/create-robots-txt).

## 콘텐츠와 canonical 운영

소개 페이지는 네이버 원문을 그대로 복제하지 않고 읽을 지점과 맥락을 정리했습니다. 따라서 각 소개 페이지는 자기 자신의 GitHub Pages 주소를 canonical로 사용하고, 네이버는 명확한 원문 링크 및 구조화 데이터의 출처로 연결했습니다. 모든 canonical을 네이버로 지정하면 GitHub 소개 페이지를 검색에 노출시키려는 의도와 맞지 않을 수 있습니다. canonical은 Google에 주는 신호이며 최종 선택을 강제하지 않습니다. [canonical 공식 안내](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls).

소개 자체에서도 읽을 가치가 있도록 실제 정보와 주제 간 연결을 유지하세요. 지역명·검색어만 바꾼 유사 페이지를 양산하거나 사용자와 검색엔진에 다른 내용을 제공하지 않습니다. [Google 스팸 정책의 도어웨이 관련 안내](https://developers.google.com/search/docs/essentials/spam-policies#doorway-abuse).

네이버 이동 수를 측정하는 분석 도구는 아직 설치하지 않았습니다. Search Console에서 확인하는 검색 유입과 실제 네이버 원문 클릭은 다른 지표입니다. 향후 필요하면 사용자가 선택한 분석 도구의 외부 링크 클릭 이벤트를 별도로 설정할 수 있습니다.

## 누적·날짜별 목록 운영

현재 사이트는 사진과 장식 이미지 없이 제목·날짜·요약·출처를 읽을 수 있는 HTML을 제공합니다. 이미지는 Google 일반 검색 색인의 필수 요소가 아니며 이미지 검색이나 시각적 검색 기능을 목표로 할 때 별도로 검토할 수 있습니다. [SEO 시작 가이드](https://developers.google.com/search/docs/fundamentals/seo-starter-guide), [이미지 검색 안내](https://developers.google.com/search/docs/appearance/google-images).

메인에는 최신 10개만, 전체 기록에는 저장된 모든 글을 유지합니다. 실제 글이 있는 연도와 월을 생성하고, 월별·주제별 목록은 30개 단위로 나눕니다. 각 목록 페이지는 고유 URL과 self canonical을 갖고 이전·다음 페이지를 실제 HTML 링크로 연결합니다. 모든 목록을 1페이지로 canonical 처리하지 않습니다. [Google 페이지 나누기 안내](https://developers.google.com/search/docs/specialty/ecommerce/pagination-and-incremental-page-loading).

새 글을 발견하는 수단으로 RSS를 사용할 수 있으나, RSS의 최신 목록만으로 전체 저장 데이터를 덮어쓰면 과거 글을 잃게 됩니다. 원문 ID로 중복을 구분하고 새 항목만 추가해야 합니다. 현재는 수동으로 원문을 읽고 소개를 추가한 뒤 정적 파일을 생성하는 방식입니다. 향후 일일 작업을 연결하더라도 제목·게시일·본문 접근 여부를 확인하고, 미확인 요약이나 비어 있는 소개 페이지를 자동 게시하지 않는 기준을 유지하세요. 이번 작업에서 예약 작업이나 GitHub Actions 자동 수집은 설정하지 않았습니다.
