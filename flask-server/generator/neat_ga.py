# import copy
# import warnings

# import matplotlib.pyplot as plt
# import numpy as np
# import multiprocessing
# import os
# import graphviz
# import pickle

# # import neat
# import neat_dtr
# import generator.query as query


# def plot_stats(statistics, ylog=False, view=False, filename='avg_fitness.svg'):
#     """ Plots the population's average and best fitness. """
#     if plt is None:
#         warnings.warn(
#             "This display is not available due to a missing optional dependency (matplotlib)"
#         )
#         return

#     generation = range(len(statistics.most_fit_genomes))
#     best_fitness = [c.fitness for c in statistics.most_fit_genomes]
#     avg_fitness = np.array(statistics.get_fitness_mean())
#     stdev_fitness = np.array(statistics.get_fitness_stdev())

#     plt.plot(generation, avg_fitness, 'b-', label="average")
#     #plt.plot(generation, avg_fitness - stdev_fitness, 'g-.', label="-1 sd")
#     plt.plot(generation, avg_fitness + stdev_fitness, 'g-.', label="+1 sd")
#     plt.plot(generation, best_fitness, 'r-', label="best")

#     plt.title("Population's average and best fitness")
#     plt.xlabel("Generations")
#     plt.ylabel("Fitness")
#     plt.grid()
#     plt.legend(loc="best")
#     if ylog:
#         plt.gca().set_yscale('symlog')

#     plt.savefig(filename)
#     if view:
#         plt.show()

#     plt.close()


# def plot_spikes(spikes, view=False, filename=None, title=None):
#     """ Plots the trains for a single spiking neuron. """
#     if plt is None:
#         warnings.warn(
#             "This display is not available due to a missing optional dependency (matplotlib)"
#         )
#         return

#     t_values = [t for t, I, v, u in spikes]
#     v_values = [v for t, I, v, u in spikes]
#     u_values = [u for t, I, v, u in spikes]
#     I_values = [I for t, I, v, u in spikes]

#     fig = plt.figure()
#     plt.subplot(3, 1, 1)
#     plt.ylabel("Potential (mv)")
#     plt.xlabel("Time (in ms)")
#     plt.grid()
#     plt.plot(t_values, v_values, "g-")

#     if title is None:
#         plt.title("Izhikevich's spiking neuron model")
#     else:
#         plt.title("Izhikevich's spiking neuron model ({0!s})".format(title))

#     plt.subplot(3, 1, 2)
#     plt.ylabel("Recovery (u)")
#     plt.xlabel("Time (in ms)")
#     plt.grid()
#     plt.plot(t_values, u_values, "r-")

#     plt.subplot(3, 1, 3)
#     plt.ylabel("Current (I)")
#     plt.xlabel("Time (in ms)")
#     plt.grid()
#     plt.plot(t_values, I_values, "r-o")

#     if filename is not None:
#         plt.savefig(filename)

#     if view:
#         plt.show()
#         plt.close()
#         fig = None

#     return fig


# def plot_species(statistics, view=False, filename='speciation.svg'):
#     """ Visualizes speciation throughout evolution. """
#     if plt is None:
#         warnings.warn(
#             "This display is not available due to a missing optional dependency (matplotlib)"
#         )
#         return

#     species_sizes = statistics.get_species_sizes()
#     num_generations = len(species_sizes)
#     curves = np.array(species_sizes).T

#     fig, ax = plt.subplots()
#     ax.stackplot(range(num_generations), *curves)

#     plt.title("Speciation")
#     plt.ylabel("Size per Species")
#     plt.xlabel("Generations")

#     plt.savefig(filename)

#     if view:
#         plt.show()

#     plt.close()


# def draw_net(config,
#              genome,
#              view=False,
#              filename=None,
#              node_names=None,
#              show_disabled=True,
#              prune_unused=False,
#              node_colors=None,
#              fmt='svg'):
#     """ Receives a genome and draws a neural network with arbitrary topology. """
#     # Attributes for network nodes.
#     if graphviz is None:
#         warnings.warn(
#             "This display is not available due to a missing optional dependency (graphviz)"
#         )
#         return

#     if node_names is None:
#         node_names = {}

#     assert type(node_names) is dict

#     if node_colors is None:
#         node_colors = {}

#     assert type(node_colors) is dict

#     node_attrs = {
#         'shape': 'circle',
#         'fontsize': '9',
#         'height': '0.2',
#         'width': '0.2'
#     }

#     dot = graphviz.Digraph(format=fmt, node_attr=node_attrs)

#     inputs = set()
#     for k in config.genome_config.input_keys:
#         inputs.add(k)
#         name = node_names.get(k, str(k))
#         input_attrs = {
#             'style': 'filled',
#             'shape': 'box',
#             'fillcolor': node_colors.get(k, 'lightgray')
#         }
#         dot.node(name, _attributes=input_attrs)

#     outputs = set()
#     for k in config.genome_config.output_keys:
#         outputs.add(k)
#         name = node_names.get(k, str(k))
#         node_attrs = {
#             'style': 'filled',
#             'fillcolor': node_colors.get(k, 'lightblue')
#         }

#         dot.node(name, _attributes=node_attrs)

#     if prune_unused:
#         connections = set()
#         for cg in genome.connections.values():
#             if cg.enabled or show_disabled:
#                 connections.add(cg.key)

#         used_nodes = copy.copy(outputs)
#         pending = copy.copy(outputs)
#         while pending:
#             new_pending = set()
#             for a, b in connections:
#                 if b in pending and a not in used_nodes:
#                     new_pending.add(a)
#                     used_nodes.add(a)
#             pending = new_pending
#     else:
#         used_nodes = set(genome.nodes.keys())

#     for n in used_nodes:
#         if n in inputs or n in outputs:
#             continue

#         attrs = {'style': 'filled', 'fillcolor': node_colors.get(n, 'white')}
#         dot.node(str(n), _attributes=attrs)

#     for cg in genome.connections.values():
#         if cg.enabled or show_disabled:
#             #if cg.input not in used_nodes or cg.output not in used_nodes:
#             #    continue
#             input, output = cg.key
#             a = node_names.get(input, str(input))
#             b = node_names.get(output, str(output))
#             style = 'solid' if cg.enabled else 'dotted'
#             color = 'green' if cg.weight > 0 else 'red'
#             width = str(0.1 + abs(cg.weight / 5.0))
#             dot.edge(a,
#                      b,
#                      _attributes={
#                          'style': style,
#                          'color': color,
#                          'penwidth': width
#                      })

#     dot.render(filename, view=view)

#     return dot


# runs_per_net = 2


# # Use the NN network phenotype and the discrete actuator force function.
# def eval_genome(genome, config):
#     net = neat.nn.FeedForwardNetwork.create(genome, config)

#     fitnesses = []

#     for runs in range(runs_per_net):
#         modules = query.db_query()
#         data = neat_dtr.Data()
#         data.MCTS_reset()
#         fitness = 0.0

#         for m in modules:
#             inputs = data.neat_inputs(m)
#             raw_output = net.activate(inputs)
#             raw_output = raw_output[0]

#             ##convert from [-1, 1] to [0, 2]
#             raw_output = raw_output + 1
#             ## (0,2) to (0, 5120)
#             raw_output = raw_output * 1279.5 * 2

#             ## convert to an integer in range [0, 2560]
#             output = raw_output // 2

#             schedule = data.get_scheduling_data(output)

#             m["days"] = schedule["days"]
#             m["timeslots"] = schedule["timeslots"]
#             m["room"] = schedule["room"]

#             data.mcts_schedule(m)

#         fitness += data.get_score(modules)
#         fitnesses.append(fitness)

#     # The genome's fitness is its worst performance across all runs.
#     return min(fitnesses)


# def eval_genomes(genomes, config):
#     for genome_id, genome in genomes:
#         genome.fitness = eval_genome(genome, config)


# def run(generations):
#     # Load the config file, which is assumed to live in
#     # the same directory as this script.
#     local_dir = os.path.dirname(__file__)
#     config_path = os.path.join(local_dir, 'config-feedforward')
#     config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
#                          neat.DefaultSpeciesSet, neat.DefaultStagnation,
#                          config_path)

#     pop = neat.Population(config)
#     stats = neat.StatisticsReporter()
#     pop.add_reporter(stats)
#     pop.add_reporter(neat.StdOutReporter(True))

#     pe = neat.ParallelEvaluator(multiprocessing.cpu_count(), eval_genome)
#     winner = pop.run(pe.evaluate, generations)

#     # Save the winner.
#     with open('winner-feedforward', 'wb') as f:
#         pickle.dump(winner, f)

#     #print(winner)

#     plot_stats(stats, ylog=True, view=True, filename="feedforward-fitness.svg")
#     plot_species(stats, view=True, filename="feedforward-speciation.svg")

#     node_names = {-1: 'x', -2: 'dx', -3: 'theta', -4: 'dtheta', 0: 'control'}
#     draw_net(config, winner, True, node_names=node_names)

#     draw_net(config,
#              winner,
#              view=True,
#              node_names=node_names,
#              filename="winner-feedforward.gv")
#     draw_net(config,
#              winner,
#              view=True,
#              node_names=node_names,
#              filename="winner-feedforward-enabled.gv",
#              show_disabled=False)
#     draw_net(config,
#              winner,
#              view=True,
#              node_names=node_names,
#              filename="winner-feedforward-enabled-pruned.gv",
#              show_disabled=False,
#              prune_unused=True)


# if __name__ == '__main__':
#     run(10)


# def results():

#     with open('winner-feedforward', 'rb') as f:
#         c = pickle.load(f)
#     print("Loaded genome:")
#     print(c)

#     config_path = '/content/drive/My Drive/agroecology/Config'
#     config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
#                          neat.DefaultSpeciesSet, neat.DefaultStagnation,
#                          config_path)

#     net = neat.nn.FeedForwardNetwork.create(c, config)

#     modules = query.db_query()
#     data = neat_dtr.Data()
#     data.MCTS_reset()
#     fitness = 0.0

#     for m in modules:
#         inputs = data.neat_inputs(m)
#         raw_output = net.activate(inputs)
#         raw_output = raw_output[0]

#         ##convert from [-1, 1] to [0, 2]
#         raw_output = raw_output + 1
#         ## (0,2) to (0, 5120)
#         raw_output = raw_output * 1279.5 * 2

#         ## convert to an integer in range [0, 2560]
#         output = raw_output // 2

#         schedule = data.get_scheduling_data(output)

#         m["days"] = schedule["days"]
#         m["timeslots"] = schedule["timeslots"]
#         m["room"] = schedule["room"]

#         data.mcts_schedule(m)

#     fitness += data.get_score(modules)
#     print("best fitness", fitness)
#     return modules
