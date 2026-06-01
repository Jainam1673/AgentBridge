import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { Brain, Cpu, Zap } from 'lucide-react';

export default function MLModelsPage() {
  const models = [
    { name: 'Ticket Router', type: 'XGBoost', accuracy: '94.5%', status: 'Active', version: 'v2.1.0' },
    { name: 'Priority Predictor', type: 'PyTorch', accuracy: '91.2%', status: 'Training', version: 'v1.0.4-rc' },
    { name: 'Recommendation Engine', type: 'XGBoost', accuracy: '88.7%', status: 'Active', version: 'v3.2.1' },
  ];

  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-bold">Machine Learning Layer</h1>
      
      <div className="grid gap-6 md:grid-cols-3">
        <Card>
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium">Model Health</CardTitle>
            <Zap className="h-4 w-4 text-yellow-500" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">Optimal</div>
            <p className="text-xs text-muted-foreground">All active models within SLA</p>
          </CardContent>
        </Card>
        <Card>
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium">Training Pipeline</CardTitle>
            <Cpu className="h-4 w-4 text-blue-500" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">Running</div>
            <p className="text-xs text-muted-foreground">Priority Predictor re-training</p>
          </CardContent>
        </Card>
        <Card>
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium">Drift Detection</CardTitle>
            <Brain className="h-4 w-4 text-purple-500" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">None</div>
            <p className="text-xs text-muted-foreground">No distribution shift detected</p>
          </CardContent>
        </Card>
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Model Registry</CardTitle>
        </CardHeader>
        <CardContent>
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>Model Name</TableHead>
                <TableHead>Type</TableHead>
                <TableHead>Accuracy</TableHead>
                <TableHead>Status</TableHead>
                <TableHead>Version</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {models.map((model) => (
                <TableRow key={model.name}>
                  <TableCell className="font-bold">{model.name}</TableCell>
                  <TableCell>{model.type}</TableCell>
                  <TableCell>{model.accuracy}</TableCell>
                  <TableCell>
                    <Badge variant={model.status === 'Active' ? 'default' : 'secondary'}>
                      {model.status}
                    </Badge>
                  </TableCell>
                  <TableCell className="font-mono text-xs">{model.version}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </CardContent>
      </Card>
    </div>
  );
}
