import { NextRequest, NextResponse } from 'next/server';
import { verifyRole } from '@/lib/auth';
import { FaultService, FaultCategory } from '@/services/fault.service';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest) {
  try {
    const admin = await verifyRole(req, 'admin');
    if (!admin) {
      return NextResponse.json({ message: 'Unauthorized. Admin access required.' }, { status: 403 });
    }

    const categories = await FaultService.getCategories();
    return NextResponse.json({ success: true, categories });
  } catch (error: any) {
    console.error('API get fault categories error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

export async function POST(req: NextRequest) {
  try {
    const admin = await verifyRole(req, 'admin');
    if (!admin) {
      return NextResponse.json({ message: 'Unauthorized. Admin access required.' }, { status: 403 });
    }

    const body = await req.json();
    const { id, name, category, target, icon } = body;

    if (!name || !name.trim()) {
      return NextResponse.json({ message: 'Category name is required.' }, { status: 400 });
    }

    const current = await FaultService.getCategories();
    const cleanId = id ? id.trim() : name.trim().toLowerCase().replace(/[^a-z0-9]/g, '_');

    const existingIndex = current.findIndex(c => c.id === cleanId);
    const newCategory: FaultCategory = {
      id: cleanId,
      name: name.trim(),
      category: category || 'custom',
      target: target || 'student',
      icon: icon || '📌',
      isDefault: false
    };

    if (existingIndex >= 0) {
      current[existingIndex] = { ...current[existingIndex], ...newCategory };
    } else {
      current.push(newCategory);
    }

    await FaultService.saveCategories(current);

    return NextResponse.json({
      success: true,
      message: 'Fault category saved successfully.',
      categories: current
    });
  } catch (error: any) {
    console.error('API save fault category error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

export async function DELETE(req: NextRequest) {
  try {
    const admin = await verifyRole(req, 'admin');
    if (!admin) {
      return NextResponse.json({ message: 'Unauthorized. Admin access required.' }, { status: 403 });
    }

    const { searchParams } = new URL(req.url);
    const categoryId = searchParams.get('id');

    if (!categoryId) {
      return NextResponse.json({ message: 'Missing category id.' }, { status: 400 });
    }

    const current = await FaultService.getCategories();
    const filtered = current.filter(c => c.id !== categoryId || c.isDefault);

    await FaultService.saveCategories(filtered);

    return NextResponse.json({
      success: true,
      message: 'Fault category removed successfully.',
      categories: filtered
    });
  } catch (error: any) {
    console.error('API delete fault category error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
