import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { Badge } from "@/components/ui/badge";

export default function EvaluationsPage() {
  const evaluations = [
    { id: 'ev_1', query: 'What is our policy on data encryption?', accuracy: 0.95, relevance: 0.92, groundedness: 0.98, status: 'Passed' },
    { id: 'ev_2', query: 'Create a summary of recent Jira tickets for Acme.', accuracy: 0.88, relevance: 0.90, groundedness: 0.85, status: 'Passed' },
    { id: 'ev_3', query: 'Predict the escalation priority for ticket #402.', accuracy: 0.92, relevance: 0.95, groundedness: 0.90, status: 'Passed' },
    { id: 'ev_4', query: 'How many files are in the Globex Drive?', accuracy: 1.0, relevance: 1.0, groundedness: 1.0, status: 'Passed' },
  ];

  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-bold">Evaluation Framework</h1>
      
      <div className="grid gap-6 md:grid-cols-3">
        <Card>
          <CardHeader>
            <CardTitle className="text-sm font-medium">Mean Accuracy</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">93.7%</div>
          </CardContent>
        </Card>
        <Card>
          <CardHeader>
            <CardTitle className="text-sm font-medium">Mean Groundedness</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">91.2%</div>
          </CardContent>
        </Card>
        <Card>
          <CardHeader>
            <CardTitle className="text-sm font-medium">Hallucination Rate</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">1.4%</div>
          </CardContent>
        </Card>
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Detailed Evaluations</CardTitle>
        </CardHeader>
        <CardContent>
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>Query</TableHead>
                <TableHead>Accuracy</TableHead>
                <TableHead>Relevance</TableHead>
                <TableHead>Groundedness</TableHead>
                <TableHead>Status</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {evaluations.map((ev) => (
                <TableRow key={ev.id}>
                  <TableCell className="max-w-[300px] truncate">{ev.query}</TableCell>
                  <TableCell>{(ev.accuracy * 100).toFixed(0)}%</TableCell>
                  <TableCell>{(ev.relevance * 100).toFixed(0)}%</TableCell>
                  <TableCell>{(ev.groundedness * 100).toFixed(0)}%</TableCell>
                  <TableCell>
                    <Badge variant="outline" className="bg-green-500/10 text-green-500 border-green-500/20">
                      {ev.status}
                    </Badge>
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </CardContent>
      </Card>
    </div>
  );
}
