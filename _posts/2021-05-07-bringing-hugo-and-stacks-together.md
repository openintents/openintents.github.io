---
title: "Bringing Hugo and Stacks together"
categories: blockstack
image:
  title: bringing-hugo-and-stacks-together.jpg
---

[Hugo](https://gohugo.io/) is a static site generator framework. It is open source and fast. The site for Friedger Pool is using it. We wanted to add a more personalized experience to that site and therefore, the site should become a Stacks app. That means that the app uses the Stacks authentication provided by the [@stacks/connect](https://github.com/blockstack/connect) library.

It is possible to add React single page app into a hugo site as demonstrated by [Kai Hendry](https://github.com/kaihendry/react-hugo-esbuild) using esbuild. Unfortunately, the connect library does not play nicely with esbuild. Polyfills are missing. We didn't want to handle these. We decided to keep the Hugo part and the React part separate and then merge the two static parts for publishing.

The result is a git repo with a `hugo` folder and a `stacks`folder. In the Hugo site we add to one page  a `div` that will contain the react app. That generated page ideally is `index.html` in a subfolder (e.g. `members`). This `index.html` page is copied over to the react app into the `public` folder of the react app. Now the react app can find the `div` for rendering. After creating the production build with `yarn build` (from create-react-app), the files from need to be copied into the root folder that contains the site for publishing. The files of react's `static` folder go next to the files of hugo's `public` folder. React's `index.html` goes into hugo's subfolder replacing the `index.html` that we copied over to the react folder earlier. This can be done in a single script:

`cd packages/hugo
hugo -D
cp public/members/index.html ../react/public
cd ../react
yarn build
cd ../..
cp -r packages/hugo/public .
cp -r packages/react/build/static public
cp packages/react/build/* public/members`

Now you can serve the public folder and have a hugo site with a react app.

The source code for Friedger Pool's site is available on [github](https://github.com/friedger/stacking/tree/dev).
