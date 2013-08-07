#-*- coding:utf-8 -*-
import trees
import treePlotter

fr = open('lenses.txt')
lenses = [inst.strip().split('\t') for inst in fr.readlines()]
lensesLables = ['age', 'prescript', 'astigmatic', 'tearRate']
lensesTree = trees.createTree(lenses, lensesLables)
print lensesTree

treePlotter.createPlot(lensesTree)