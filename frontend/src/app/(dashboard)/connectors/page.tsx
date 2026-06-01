import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Github, HardDrive, Trello, Database } from 'lucide-react';

export default function ConnectorsPage() {
  const connectors = [
    { name: 'Google Drive', icon: HardDrive, status: 'Connected', lastSync: '10m ago', items: '1,240 docs' },
    { name: 'GitHub', icon: Github, status: 'Connected', lastSync: '1h ago', items: '42 repos' },
    { name: 'Jira', icon: Trello, status: 'Connected', lastSync: '5m ago', items: '850 tickets' },
    { name: 'PostgreSQL', icon: Database, status: 'Healthy', lastSync: 'Live', items: '12 tables' },
  ];

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h1 className="text-3xl font-bold">Enterprise Connectors</h1>
        <Button>Add New Connector</Button>
      </div>

      <div className="grid gap-6 md:grid-cols-2">
        {connectors.map((connector) => (
          <Card key={connector.name}>
            <CardHeader className="flex flex-row items-center justify-between pb-2">
              <div className="flex items-center gap-3">
                <connector.icon className="h-6 w-6" />
                <CardTitle className="text-xl font-bold">{connector.name}</CardTitle>
              </div>
              <Badge variant="outline" className="bg-green-500/10 text-green-500 hover:bg-green-500/10 border-green-500/20">
                {connector.status}
              </Badge>
            </CardHeader>
            <CardContent>
              <div className="grid grid-cols-2 gap-4 text-sm">
                <div>
                  <div className="text-muted-foreground">Last Sync</div>
                  <div className="font-medium">{connector.lastSync}</div>
                </div>
                <div>
                  <div className="text-muted-foreground">Items Synced</div>
                  <div className="font-medium">{connector.items}</div>
                </div>
              </div>
              <div className="mt-4 flex gap-2">
                <Button variant="outline" size="sm">Configure</Button>
                <Button variant="outline" size="sm">Sync Now</Button>
              </div>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
}
