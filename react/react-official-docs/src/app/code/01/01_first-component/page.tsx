import Gallery, { Profile } from "@/components/01/Gallery";
import React from "react";

function MainProfile() {
  return <img src="https://i.imgur.com/MK3eW3As.jpg" alt="Katherine Johnson" />;
}

export default function Page() {
  return (
    <div className="flex flex-col max-w-4xl mx-auto pt-20 px-5 min-h-screen bg-gray-50">
      <h1 className="text-4xl font-bold mb-8 text-center">UI 표현하기</h1>
      <div className="space-y-8">
        {/* first-component */}
        <article id="first-component">
          <h2 className="text-2xl font-semibold">01.첫 번째 컴포넌트</h2>
          <div className="flex">
            <MainProfile />
            <MainProfile />
            <MainProfile />
          </div>
        </article>

        {/* importing-and-exporting */}
        <article id="importing-and-exporting">
          <h2 className="text-2xl font-semibold">
            02. 컴포넌트 Import 및 Export하기
          </h2>
          <div>
            <Profile />
            <Gallery />
          </div>
        </article>

        {/* markup-with-tsx */}
        <article id="markup-with-tsx">
          <h2 className="text-2xl font-semibold">03. TSX로 마크업 작성하기</h2>
          <div>
            <Profile />
            <Gallery />
          </div>
        </article>

        {/* curly-braces */}
        <article id="curly-braces">
          <h2 className="text-2xl font-semibold">
            04. 중괄호가 있는 TSX에서 자바스크립트 사용하기
          </h2>
          <div>
            <Profile />
            <Gallery />
          </div>
        </article>

        {/* passing-props */}
        <article id="passing-props">
          <h2 className="text-2xl font-semibold">
            05. 컴포넌트에 Props 전달하기
          </h2>
          <div>
            <Profile />
            <Gallery />
          </div>
        </article>

        {/* conditional-rendering */}
        <article id="conditional-rendering">
          <h2 className="text-2xl font-semibold">06. 조건부 렌더링</h2>
          <div>
            <Profile />
            <Gallery />
          </div>
        </article>

        {/* rendering-lists */}
        <article id="rendering-lists">
          <h2 className="text-2xl font-semibold">07. 리스트 렌더링</h2>
          <div>
            <Profile />
            <Gallery />
          </div>
        </article>

        {/* components-pure */}
        <article id="components-pure">
          <h2 className="text-2xl font-semibold">
            08. 컴포넌트를 순수하게 유지하기
          </h2>
          <div>
            <Profile />
            <Gallery />
          </div>
        </article>

        {/* ui-as-a-tree */}
        <article id="ui-as-a-tree">
          <h2 className="text-2xl font-semibold">09. 트리로서의 UI</h2>
          <div>
            <Profile />
            <Gallery />
          </div>
        </article>
      </div>
    </div>
  );
}
