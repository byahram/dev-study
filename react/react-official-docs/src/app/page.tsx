import Accordion from "@/components/layout/Accordion";
import { getAllPosts } from "@/utils/posts";

type Section = {
  title: string;
  content: {
    title: string;
    href: string;
  }[];
};

function groupPostsByCategory(posts: Awaited<ReturnType<typeof getAllPosts>>) {
  const grouped: Record<string, Section["content"]> = {};

  posts.forEach((post) => {
    if (!grouped[post.category]) {
      grouped[post.category] = [];
    }

    grouped[post.category].push({
      title: post.title,
      href: `/${post.category}/${post.slug}`,
    });
  });

  return Object.entries(grouped).map(([category, content]) => ({
    title: category,
    content,
  }));
}

export default function Page() {
  const posts = getAllPosts();
  const sections = groupPostsByCategory(posts);

  return (
    <div className="min-h-screen max-w-4xl flex justify-center p-4 bg-white dark:bg-black text-black dark:text-white mx-auto mt-20">
      <Accordion sections={sections} />
    </div>
  );
}
