import Link from 'next/link';
import { 
  LayoutDashboard, 
  Database, 
  Link as LinkIcon, 
  Bot, 
  LineChart, 
  Activity, 
  Settings,
  Shield,
  Cpu
} from 'lucide-react';

const navItems = [
  { href: '/overview', label: 'Overview', icon: LayoutDashboard },
  { href: '/data-readiness', label: 'Data Readiness', icon: Database },
  { href: '/connectors', label: 'Connectors', icon: LinkIcon },
  { href: '/agents', label: 'Agents', icon: Bot },
  { href: '/evaluations', label: 'Evaluations', icon: LineChart },
  { href: '/ml-models', label: 'ML Models', icon: Cpu },
  { href: '/security', label: 'Security', icon: Shield },
  { href: '/traces', label: 'Traces', icon: Activity },
  { href: '/settings', label: 'Settings', icon: Settings },
];

export function Sidebar() {
  return (
    <div className="flex h-full w-64 flex-col border-r bg-muted/20">
      <div className="flex h-14 items-center border-b px-6">
        <span className="text-lg font-bold">AgentBridge</span>
      </div>
      <nav className="flex-1 space-y-1 px-4 py-4">
        {navItems.map((item) => (
          <Link
            key={item.href}
            href={item.href}
            className="flex items-center gap-3 rounded-lg px-3 py-2 text-sm font-medium hover:bg-muted transition-colors"
          >
            <item.icon className="h-4 w-4" />
            {item.label}
          </Link>
        ))}
      </nav>
    </div>
  );
}
