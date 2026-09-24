export default async function Page({
  searchParams,
}: {
  searchParams?: Promise<{ [key: string]: string | string[] | undefined }>;
}) {
  const resolvedParams = searchParams ? await searchParams : undefined;
  const queryString = resolvedParams
    ? new URLSearchParams(
        Object.entries(resolvedParams).flatMap(([k, v]) =>
          Array.isArray(v) ? v.map((item) => [k, item]) : v !== undefined ? [[k, v]] : []
        )
      ).toString()
    : '';

  const iframeSrc = queryString ? `/index.html?${queryString}` : '/index.html';

  return (
    <main style={{ width: '100vw', height: '100vh', margin: 0, padding: 0, overflow: 'hidden' }}>
      <iframe
        src={iframeSrc}
        title="BetBonus — Premium Rewards Platform"
        style={{
          width: '100%',
          height: '100%',
          border: 'none',
          display: 'block',
        }}
      />
    </main>
  );
}
