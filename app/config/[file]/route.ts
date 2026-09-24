import { NextRequest, NextResponse } from 'next/server';
import fs from 'fs';
import path from 'path';

export async function GET(
  request: NextRequest,
  context: { params: Promise<{ file: string }> }
) {
  try {
    const { file } = await context.params;
    // Sanitize file name to prevent path traversal
    const safeFile = path.basename(file);
    const filePath = path.join(process.cwd(), 'config', safeFile);

    if (fs.existsSync(filePath)) {
      const content = fs.readFileSync(filePath, 'utf-8');
      return new NextResponse(content, {
        status: 200,
        headers: {
          'Content-Type': 'application/javascript; charset=utf-8',
          'Cache-Control': 'no-store, no-cache, must-revalidate',
        },
      });
    }

    return new NextResponse(`// Config file ${safeFile} not found`, {
      status: 404,
      headers: { 'Content-Type': 'application/javascript; charset=utf-8' },
    });
  } catch (err) {
    return new NextResponse(`// Error loading config: ${String(err)}`, {
      status: 500,
      headers: { 'Content-Type': 'application/javascript; charset=utf-8' },
    });
  }
}
