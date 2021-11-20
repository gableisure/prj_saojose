import * as React from 'react';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemText from '@mui/material/ListItemText';
import ListItemAvatar from '@mui/material/ListItemAvatar';
import Avatar from '@mui/material/Avatar';
import ArrowForwardIcon from '@mui/icons-material/ArrowForward';
import Tooltip from '@mui/material/Tooltip';
import IconButton from '@mui/material/IconButton';
import styles from './ListSpecialty.module.css';
import LocalHospitalIcon from '@mui/icons-material/LocalHospital';

export default function ListSpecialty({ specialty_name, specialty_link }) {
  return (
    <List sx={{ width: '100%', maxWidth: 360, bgcolor: 'background.paper'}}>
      <ListItem>
        <ListItemAvatar>
          <Avatar>
            <LocalHospitalIcon />
          </Avatar>
        </ListItemAvatar>
        <ListItemText primary={specialty_name}/>
        <Tooltip title="Ir">
            <IconButton href={specialty_link} target="_blank">
                <ArrowForwardIcon className={styles.icon_color}></ArrowForwardIcon>
            </IconButton>
        </Tooltip>
      </ListItem>
    </List>
  );
}
