import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { Badge } from "@/components/ui/badge";

export default function TracesPage() {
  const traces = [
    { id: 'tr_123', user: 'jack@example.com', operation: 'Document Retrieval', status: 'Success', latency: '1.2s' },
    { id: 'tr_124', user: 'admin@agentbridge.ai', operation: 'Agent Orchestration', status: 'Success', latency: '4.5s' },
    { id: 'tr_125', user: 'bob@globex.com', operation: 'BigQuery Analytics', status: 'Failed', latency: '0.8s' },
    { id: 'tr_126', user: 'alice@acme.com', operation: 'Ticket Routing', status: 'Success', latency: '1.5s' },
  ];

  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-bold">Observability & Traces</h1>
      
      <Card>
        <CardHeader>
          <CardTitle>Recent Traces (OpenTelemetry)</CardTitle>
        </CardHeader>
        <CardContent>
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>Trace ID</TableHead>
                <TableHead>User</TableHead>
                <TableHead>Operation</TableHead>
                <TableHead>Status</TableHead>
                <TableHead>Latency</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {traces.map((trace) => (
                <TableRow key={trace.id}>
                  <TableCell className="font-mono text-xs">{trace.id}</TableCell>
                  <TableCell>{trace.user}</TableCell>
                  <TableCell>{trace.operation}</TableCell>
                  <TableCell>
                    <Badge variant={trace.status === 'Success' ? 'default' : 'destructive'}>
                      {trace.status}
                    </Badge>
                  </TableCell>
                  <TableCell>{trace.latency}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </CardContent>
      </Card>
    </div>
  );
}
