import Accordion from "@/components/layout/Accordion";
import { getAllPosts, groupPostsByCategory } from "@/utils/posts";

export default function Page() {
  const posts = getAllPosts();
  const sections = groupPostsByCategory(posts);

  return (
    <div className="min-h-screen max-w-4xl flex justify-center p-4 bg-white dark:bg-black text-black dark:text-white mx-auto mt-20">
      <Accordion sections={sections} />
    </div>
  );
}
