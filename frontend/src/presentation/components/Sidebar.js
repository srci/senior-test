import Link from 'next/link';

export default function Sidebar() {
  return (
    <div className="w-64 bg-gray-800 text-white h-screen p-4">
      <h2 className="text-2xl font-bold mb-6">AutoPartsPro</h2>
      <nav>
        <ul>
          <li className="mb-4">
            <Link href="/" className="hover:text-gray-300">Home</Link>
          </li>
          <li className="mb-4">
            <Link href="/customers" className="hover:text-gray-300">Customers</Link>
          </li>
          <li className="mb-4">
            <Link href="/vehicles" className="hover:text-gray-300">Vehicles</Link>
          </li>
          <li className="mb-4">
            <Link href="/parts" className="hover:text-gray-300">Parts</Link>
          </li>
          <li className="mb-4">
            <Link href="/repair-orders" className="hover:text-gray-300">Repair Orders</Link>
          </li>
          <li className="mb-4">
            <Link href="/order-details" className="hover:text-gray-300">Order Details</Link>
          </li>
          <li className="mb-4">
            <Link href="/optimize" className="hover:text-gray-300">Optimize</Link>
          </li>
        </ul>
      </nav>
    </div>
  );
}