import fs from "fs";
import path from "path";
import matter from "gray-matter";
import { compileMDX } from "next-mdx-remote/rsc";
import remarkGfm from "remark-gfm";
import rehypeSlug from "rehype-slug";
import rehypeAutolinkHeadings from "rehype-autolink-headings";
import { notFound } from "next/navigation";
import NavigationButtons from "@/components/layout/NavigationButtons";

interface Props {
  params: {
    category: string;
    slug: string;
  };
}

const components = {
  h1: (props: React.HTMLAttributes<HTMLHeadingElement>) => (
    <h1 className="text-4xl font-bold mb-6" {...props} />
  ),
  h2: (props: React.HTMLAttributes<HTMLHeadingElement>) => (
    <h2 className="text-2xl font-semibold mt-5 mb-3" {...props} />
  ),
  pre: (props: React.HTMLAttributes<HTMLPreElement>) => (
    <pre
      className="bg-neutral-600 text-white p-4 rounded-md overflow-x-auto my-4"
      {...props}
    />
  ),
  code: (props: React.HTMLAttributes<HTMLElement>) => (
    <code className="bg-gray-100 text-red-600 px-1 py-0.5 rounded" {...props} />
  ),
  a: (props: React.AnchorHTMLAttributes<HTMLAnchorElement>) => (
    <a className="text-blue-600 underline" {...props} />
  ),
};

export default async function PostDetail({ params }: Props) {
  const { category, slug } = params;

  const filePath = path.join(
    process.cwd(),
    "src",
    "posts",
    category,
    `${slug}.mdx`
  );

  try {
    const fileContent = fs.readFileSync(filePath, "utf8");
    const { content } = matter(fileContent);

    const compiled = await compileMDX({
      source: content,
      options: {
        mdxOptions: {
          remarkPlugins: [remarkGfm],
          rehypePlugins: [rehypeSlug, rehypeAutolinkHeadings],
        },
      },
      components,
    });

    return (
      <>
        <article className="prose dark:prose-invert max-w-4xl mx-auto mt-20 p-4">
          <NavigationButtons />
          {compiled.content}
        </article>
      </>
    );
  } catch (error) {
    console.error("❌ MDX 파싱 실패:", error);
    notFound();
  }
}
