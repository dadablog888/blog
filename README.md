# 나의 GitHub 블로그

GitHub Pages에서 제공하는 간단한 HTML 블로그입니다.

## 로컬 확인

`index.html`을 브라우저로 열면 `Hello World`가 표시됩니다.

## 커밋과 업로드

저장소 폴더에서 아래 명령을 순서대로 실행합니다.

```sh
git diff
git add index.html README.md .gitignore
git diff --cached
git commit -m "feat: add Hello World blog page"
git push origin main
```

커밋은 변경 내용을 로컬 Git 기록에 저장하고, push는 커밋을 GitHub로 업로드합니다.

## GitHub Pages 설정

1. GitHub 저장소의 **Settings → Pages**를 엽니다.
2. **Build and deployment → Source**에서 **Deploy from a branch**를 선택합니다.
3. **Branch**를 `main`, 폴더를 `/ (root)`로 선택하고 **Save**를 누릅니다.
4. 배포가 완료되면 <https://dadablog888.github.io/blog/>에서 확인합니다.

이후 `main` 브랜치에 변경 내용을 push하면 사이트가 다시 배포됩니다.
