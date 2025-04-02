import fs from "fs";
import path from "path";
import matter from "gray-matter";

export interface BlogPostMeta {
  title: string;
  date: string;
  tags?: string[];
  description?: string;
  slug: string;
  category: string;
}

const postsDirectory = path.join(process.cwd(), "src", "posts");

// 모든 게시물 가져오기
export function getAllPosts(): BlogPostMeta[] {
  const categories = fs.readdirSync(postsDirectory);

  const posts = categories.flatMap((category) => {
    const dir = path.join(postsDirectory, category);
    const files = fs.readdirSync(dir);

    return files.map((filename) => {
      const filePath = path.join(dir, filename);
      const fileContent = fs.readFileSync(filePath, "utf8");
      const { data } = matter(fileContent);
      const slug = filename.replace(/\.mdx$/, "");

      return {
        ...(data as Omit<BlogPostMeta, "slug" | "category">),
        slug,
        category,
      };
    });
  });

  return posts.sort(
    (a, b) => new Date(b.date).getTime() - new Date(a.date).getTime()
  );
}
