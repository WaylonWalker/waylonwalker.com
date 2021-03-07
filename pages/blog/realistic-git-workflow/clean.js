import { Gitgraph } from '@gitgraph/react'
import React from 'react'

const Clean = () => (
  <Gitgraph>
    {(gitgraph) => {
      const main = gitgraph.branch('main')
      main.commit('Initial Commit')
      main.commit('Feature Release')

      const feature1 = main.branch('feature1')
      feature1.commit('feature1')

      const feature = main.branch('feature_branch')
      feature.commit('FiX Formatted with Black')
      feature.commit('FEAT implemented feature into the project')
      main.merge(feature)
    }}
  </Gitgraph>
)

export default Clean
