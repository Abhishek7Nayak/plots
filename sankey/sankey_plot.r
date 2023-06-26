sankey_without_CE <- function(sanky_data_treatment_combined_withoutCE) {
  
  # Convert data to data.table for efficient manipulation
  lot <- as.data.table(sanky_data_treatment_combined_withoutCE)
  
  # Sort the data by the "line" column and filter lines up to 4
  lot <- lot[order(line)]
  lot <- lot[line <= 4]
  
  # Create a data frame of unique node names
  nodes_lot <- data.frame(name = unique(c(lot$source, lot$target)))
  
  # Assign IDline1 and IDline2 based on the node names
  lot$IDline1 <- match(lot$source, nodes_lot$name) - 1
  lot$IDline2 <- match(lot$target, nodes_lot$name) - 1
  
  fig <- plot_ly(
    type = "sankey",
    orientation = "h",
    
    node = list(
      label = nodes_lot$name,
      pad = 15,
      thickness = 20,
      coustomdata = 'test',
      line = list(
        color = "#FCDFFF",
        width = 0.5
      )
    ),
    
    link = list(
      source = lot$IDline1,
      target = lot$IDline2,
      value = lot$value
    )
  )
  
  fig <- fig %>% layout(
    title = "Basic Sankey Diagram",
    font = list(
      size = 10
    )
  )
  
  print(fig)
}
