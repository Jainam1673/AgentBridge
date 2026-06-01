import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";

export default function AgentsPage() {
  const agents = [
    { name: 'Planner Agent', status: 'Active', tasks: ['Task Decomposition', 'Planning'] },
    { name: 'Knowledge Agent', status: 'Active', tasks: ['Retrieval', 'Summarization'] },
    { name: 'Data Agent', status: 'Idle', tasks: ['Warehouse Queries', 'Analytics'] },
    { name: 'Action Agent', status: 'Active', tasks: ['Ticket Creation', 'Workflows'] },
    { name: 'Critic Agent', status: 'Active', tasks: ['Validation', 'Quality Scoring'] },
  ];

  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-bold">Multi-Agent System</h1>
      
      <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
        {agents.map((agent) => (
          <Card key={agent.name}>
            <CardHeader className="flex flex-row items-center justify-between pb-2">
              <CardTitle className="text-lg font-bold">{agent.name}</CardTitle>
              <Badge variant={agent.status === 'Active' ? 'default' : 'secondary'}>
                {agent.status}
              </Badge>
            </CardHeader>
            <CardContent>
              <div className="text-sm font-medium mb-2">Capabilities:</div>
              <ul className="list-disc list-inside text-sm text-muted-foreground">
                {agent.tasks.map((task) => (
                  <li key={task}>{task}</li>
                ))}
              </ul>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
}
