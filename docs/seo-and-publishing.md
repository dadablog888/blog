# 네이버 원문을 우선하는 검색 전략

최우선 목표는 Google 검색 유입이 **https://blog.naver.com/dadablog888** 원문으로 이어지게 하는 것입니다. **https://dadablog888.github.io/** 및 프로젝트 Pages는 보조 기록과 목차입니다. 같은 원칙을 `skills/naver-blog-update/SKILL.md`에도 명시했습니다.

## 구현 정책

- `content/site.json`: `searchStrategy: naver-first`.
- 모든 GitHub HTML: `noindex, follow`.
- noindex인 GitHub 문서를 사이트맵에 넣지 않으며 기존 `sitemap.xml`을 제거합니다.
- GitHub URL을 Search Console에 색인 요청하는 이전 절차는 사용하지 않습니다.
- HTML 크롤링은 허용해 Google이 noindex를 읽을 수 있게 합니다. robots 차단으로 noindex를 가리지 않습니다.
- 각 소개의 눈에 보이는 원문 링크와 `isBasedOn` 출처는 네이버의 해당 게시물입니다.
- 소개는 원문과 별개인 요약 문서이므로 모든 canonical을 네이버 홈 하나로 몰거나, 유사하지 않은 페이지의 canonical이 반드시 인정될 것이라고 가정하지 않습니다. GitHub의 self canonical은 문서 식별용으로 남지만 noindex에 의해 검색 제외를 요청합니다.

`noindex`는 GitHub 페이지가 검색결과에 나타나지 않도록 요청하는 방법입니다. Google이 다시 크롤링해 처리해야 하므로 즉시 반영된다고 보장하지 않습니다. 이 설정이 네이버의 순위나 평가를 이전·상승시키는 것은 아닙니다. 네이버를 우선 노출하도록 강제할 수는 없습니다.

참고: [Google noindex 공식 안내](https://developers.google.com/search/docs/crawling-indexing/block-indexing), [canonical 공식 안내](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls).

## 네이버에서 관리할 내용

원문에 구체적인 제목, 직접 확인한 경험과 설명, 자연스러운 관련 글 링크를 유지하는 것이 중심입니다. GitHub에 검색어만 바꾼 대량 요약 페이지를 만들어 네이버 검색 평가를 대신할 수 있다고 해석하지 않습니다. 원문 접근이나 검색 허용 상태에 문제가 있으면 네이버 플랫폼의 공개·검색 설정과 실제 검색결과에서 확인해야 합니다.

과거 GitHub 사이트맵을 제출했다면 Search Console에서 이전 제출 상태를 확인하고 필요하면 해당 제출을 삭제할 수 있습니다. 제출을 삭제하는 것만으로 색인이 제거되지는 않으며 HTML의 noindex가 실제 배포되어야 합니다. 이번 작업에서는 Search Console이나 네이버 설정을 변경하지 않았습니다.

## GitHub Pages 배포

정적 문서 주소는 `https://dadablog888.github.io/blog/`입니다. 기존 저장소의 Pages에서 `main`의 `/ (root)`를 사용하는 구성을 확인한 뒤 사용자가 변경 내용을 별도로 배포합니다. `.nojekyll`과 생성 HTML을 제공하므로 Pages 빌드에 Python이 필요하지 않습니다.

배포 후에는 메인과 대표 과거 소개 페이지의 공개 HTML에서 `noindex, follow`와 정확한 네이버 링크를 확인하세요. 프로젝트의 `/blog/robots.txt`는 호스트 루트 `/robots.txt`로 적용되는 파일이 아니지만, 각 HTML의 noindex는 별도로 읽힐 수 있습니다. 다른 주소를 사용한다면 사이트 설정의 URL을 바꾼 뒤 다시 생성합니다.

이 스킬과 수집·적용·생성 스크립트는 커밋·push·설정 저장·배포를 자동으로 실행하지 않습니다.
