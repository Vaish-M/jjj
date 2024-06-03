import pandas as pd
data = pd.read_csv('C:\\Users\\MOTHER\\Desktop\\placementMP\\placepredict.csv')

data.shape

from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
data['ACADEMICS'].plot(kind='hist', bins=20, title='ACADEMICS')
plt.gca().spines[['top', 'right',]].set_visible(False)
plt.savefig('acad_bar_plot.png')

plt.close()

from matplotlib import pyplot as plt
data['MOCK INTERVIEW'].plot(kind='hist', bins=20, title='MOCK INTERVIEW')
plt.gca().spines[['top', 'right',]].set_visible(False)
plt.savefig('mock_bar_plot.png')

plt.close()

data['JAVA'].plot(kind='hist', bins=20, title='JAVA')
plt.gca().spines[['top', 'right',]].set_visible(False)
plt.savefig('java_bar_plot.png')

plt.close()

data['PYTHON'].plot(kind='hist', bins=20, title='PYTHON')
plt.gca().spines[['top', 'right',]].set_visible(False)
plt.savefig('pyth_bar_plot.png')

plt.close()

data['FULL STACK DEVELOPMENT'].plot(kind='hist', bins=20, title='FULL STACK DEVELOPMENT')
plt.gca().spines[['top', 'right',]].set_visible(False)
plt.savefig('fsd_bar_plot.png')

plt.close()

data['MACHINE LEARNING'].plot(kind='hist', bins=20, title='MACHINE LEARNING')
plt.gca().spines[['top', 'right',]].set_visible(False)

plt.savefig('ml_bar_plot.png')

plt.close()

data['APTITUDE SKILLS'].plot(kind='hist', bins=20, title='APTITUDE SKILLS')
plt.gca().spines[['top', 'right',]].set_visible(False)

plt.savefig('apt_bar_plot.png')

plt.close()

data['COMMUNICATION SKILLS'].plot(kind='hist', bins=20, title='COMMUNICATION SKILLS')
plt.gca().spines[['top', 'right',]].set_visible(False)

plt.savefig('comm_bar_plot.png')

plt.close()

data.groupby('INTERNSHIPS').size().plot(kind='barh', color=sns.palettes.mpl_palette('Dark2'))
plt.gca().spines[['top', 'right',]].set_visible(False)

plt.savefig('intern_bar_plot.png')

plt.close()

data.groupby('CERTIFICATIONS DOMAIN').size().plot(kind='barh', color=sns.palettes.mpl_palette('Dark2'))
plt.gca().spines[['top', 'right',]].set_visible(False)

plt.savefig('cert_bar_plot.png')

plt.close()

data.groupby('PROJECT DOMAIN').size().plot(kind='barh', color=sns.palettes.mpl_palette('Dark2'))
plt.gca().spines[['top', 'right',]].set_visible(False)

plt.savefig('project_bar_plot.png')

plt.close()

figsize = (12, 1.2 * len(data['INTERNSHIPS'].unique()))
plt.figure(figsize=figsize)
sns.violinplot(data, x='ACADEMICS', y='INTERNSHIPS', inner='stick', palette='Dark2')
sns.despine(top=True, right=True, bottom=True, left=True)

plt.savefig('intern_violin_plot.png')

plt.close()

figsize = (12, 1.2 * len(data['CERTIFICATIONS DOMAIN'].unique()))
plt.figure(figsize=figsize)
sns.violinplot(data=data, x='ACADEMICS', y='CERTIFICATIONS DOMAIN', inner='stick', palette='Dark2')
sns.despine(top=True, right=True, bottom=True, left=True)

plt.savefig('cert_violin_plot.png')

plt.close()

data.plot(kind='scatter', x='PYTHON', y='JAVA', s=32, alpha=.8)
plt.gca().spines[['top', 'right',]].set_visible(False)
plt.savefig('janpy_scatter_plot.png')

plt.close()

data.plot(kind='scatter', x='DBMS', y='JAVA', s=32, alpha=.8)
plt.gca().spines[['top', 'right',]].set_visible(False)
plt.savefig('dbnja_scatter_plot.png')

plt.close()

data.plot(kind='scatter', x='MOCK INTERVIEW', y='PYTHON', s=32, alpha=.8)
plt.gca().spines[['top', 'right',]].set_visible(False)
plt.savefig('mknpy_scatter_plot.png')

plt.close()