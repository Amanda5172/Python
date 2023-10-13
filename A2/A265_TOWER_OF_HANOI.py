def towerofhanoi(disk, source, spare, destination):
  if disk == 1:
    print(f"Move disk {disk} from the source {source} to the destination {destination}")
    return
  towerofhanoi(disk-1, source, spare, destination)
  print(f"Move disk {disk} from the source {source} to the destination {destination}")
  
  towerofhanoi(disk-1,spare,destination,source)

towerofhanoi(3,"A","B","C")

